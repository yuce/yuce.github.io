title: Go Sample: Link Checker
date: 2009-11-14
tags: go, link checker

You should have heard about [Go](http://golang.org/), Google's new language.
To be honest, it is one of the ugliest languages I've ever used (*I mean among the ones not designed to be ugly*); but it's interesting enough, and I decided to teach myself some.

Here's the result of a few hrs of reading, searching, coding, reading again and coding: an (almost) port of Josh Marshall's [Python URL Link Checker](http://blog.joshmarshall.org/2009/11/url-checker/).
It doesn't support checking local files, but has a nice `-v` switch which lets you see all processed URLs.
So far, programming Go felt a bit like programming C++.
Also, Go links the code statically at the moment, which results in an executable of size 1.2MB for 64bit Linux.
(*DISCLAIMER: the following program is a toy, don't use it for anything serious*)

    :::go
    package main

    import "fmt"
    import "http"
    import "os"
    import "bytes"
    import "regexp"
    import "strings"
    import "container/vector"
    import "flag"

    // from Go tutorial
    func Append(slice, data[]byte) []byte {
        l := len(slice);

        if l + len(data) > cap(slice) { // reallocate
            // Allocate double what's needed, for future growth.
            newSlice := make([]byte, (l+len(data))*2);

            // Copy data (could use bytes.Copy()).
            for i, c := range slice {
                newSlice[i] = c
            }

            slice = newSlice;
        }

        slice = slice[0:l+len(data)];

        for i, c := range data {
            slice[l+i] = c
        }

        return slice;
    }

    func get_page(url string) string {
        // http.Get doesn't work well without a slash at the end
        url = url + "/";
        var content []byte;
        var buf [65535]byte;

        resp, _, e := http.Get(url);
        if e != nil {
            fmt.Println(e);
            os.Exit(1);
        }

        for true {
            rlen, e := resp.Body.Read(buf[0:len(buf)]);
            if e == os.EOF {
                break;
            }
            else if e != nil {
                fmt.Println(e);
                os.Exit(2);
            }
            content = Append(content, buf[0:rlen]);
        }

        resp.Body.Close();
        return bytes.NewBuffer(content).String();
    }

    func get_urls(page *string) []string {
        link_re, _ := regexp.Compile(`http://[^ <>"'()]+`);
        return link_re.AllMatchesString(*page, 0);
    }

    func check_url(url string) int {
        url = strings.TrimSpace(url);
        // using GET instead of HEAD, since Go has a Get function
        // and we just need the response code
        resp, _, e := http.Get(url);
        if e != nil {
            return 0;
        }
        return resp.StatusCode;
    }

    func main() {
        // parse command line arguments
        isVerbose := flag.Bool("v", false, "Display processed URLs");
        flag.Parse();
        if flag.NArg() < 1 {
            fmt.Println("Usage: checkurls [-v] URL");
            os.Exit(1);
        }
        checkedUrl := flag.Arg(0);

        fmt.Printf("Searching for URLs [%s]\n", checkedUrl);

        codes := make(map[int]*vector.StringVector);
        page := get_page(checkedUrl);
        urls := get_urls(&page);

        fmt.Printf("Checking %d URLs...\n", len(urls));

        for i := 0; i < len(urls); i++ {
            code := check_url(urls[i]);
            // if code wasn't seen before, create a vector for it in codes
            if _, ok := codes[code]; !ok {
                codes[code] = vector.NewStringVector(0);
            }
            codes[code].Push(urls[i]);
            if *isVerbose {
                fmt.Printf("[%3d] %s\n", code, urls[i]);
            }
        }

        fmt.Println("\nResults");
        fmt.Println("=======");

        for code, links := range codes {
            fmt.Printf("There were %d %ds.\n", links.Len(), code);
            if 399 < code && code < 500 {
                for i := 0; i < links.Len(); i++ {
                    fmt.Printf("* %s\n", links.At(i));
                }
            }
            fmt.Println("");
        }
    }

