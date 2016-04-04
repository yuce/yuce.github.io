title: Erlang File Upload
date: 2014-11-19
tags: erlang, file upload
draft: true

Erlang file upload


    :::erlang
    -define(CRLF, "\r\n").

    upload(Binary, FileName, FieldName, Url) ->
        BinFileName = list_to_binary(FileName),
        BinFieldName = list_to_binary(FieldName),
        Boundary = <<"Uploader">>,
        Body = <<"--", Boundary/binary, ?CRLF,
                 "Content-Disposition: form-data; name=\"",
                    BinFieldName/binary,
                    "\"; filename=\"", BinFileName/binary, "\"", ?CRLF,
                 "Content-Type: application/octet-stream", ?CRLF,
                 ?CRLF,
                 Binary/binary, ?CRLF,
                 "--", Boundary/binary, "--", ?CRLF,
                 ?CRLF>>,
        ContentType = "multipart/form-data; boundary=" ++ Boundary,
        httpc:request(post, {Url, [], ContentType, Body}, [], []).

