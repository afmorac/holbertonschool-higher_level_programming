# 1. usando curl para apis

## 1. verificar curl instalado

curl --version  
me sale esto:

curl 7.64.1 (x86_64-apple-darwin19.0) libcurl/7.64.1 (SecureTransport) LibreSSL/2.8.3 zlib/1.2.11 nghttp2/1.39.2  
Release-Date: 2019-03-27  
Protocols: dict file ftp ftps gopher http https imap imaps ldap ldaps pop3 pop3s rtsp smb smbs smtp smtps telnet tftp  
Features: AsynchDNS GSS-API HTTP2 HTTPS-proxy IPv6 Kerberos Largefile libz MultiSSL NTLM NTLM_WB SPNEGO SSL UnixSockets

---

## 2. probar cargar una pagina

curl http://google.com  
respuesta:

<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">  
<TITLE>301 Moved</TITLE></HEAD><BODY>  
<H1>301 Moved</H1>  
The document has moved <A HREF="http://www.google.com/">here</A>.  
</BODY></HTML>  

esto significa q google redirige a otra url

---

## 3. obtener posts desde jsonplaceholder (GET)

curl https://jsonplaceholder.typicode.com/posts  

me sale un monton de posts en JSON. cada uno tiene:

"userId"  
"id"  
"title"  
"body"  

---

## 4. ver solo los headers

curl -I https://jsonplaceholder.typicode.com/posts  
respuesta:

HTTP/2 200  
date: Mon, 16 Jun 2025 02:17:28 GMT  
content-type: application/json; charset=utf-8  
access-control-allow-credentials: true  
cache-control: max-age=43200  
server: cloudflare  
via: 2.0 heroku-router  
x-powered-by: Express  

esto me enseña q la api esta corriendo bien y q usa json

---

## 5. enviar datos usando POST

curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts  
respuesta:

{
  "title": "foo",
  "body": "bar",
  "userId": "1",
  "id": 101
}
