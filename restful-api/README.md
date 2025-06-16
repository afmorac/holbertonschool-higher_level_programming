# 0. basics http y https

## diferencia entre http y https

- la S en https significa secure  
- https encripta la info q se manda al server, pa q nadie la vea  
- http no tiene seguridad, la data se ve facil si alguien la intercepta  
- por eso, paginas de banco o donde uno pone contraseñas deben tener https si o si  
- https usa certificado q hace la conexion mas segura  

---

## estructura de un request y response http

esto lo vi en google.com en el network del navegador. pongo un ejemplo d lo q sale:

### request
Request URL: https://www.google.com/  
Request Method: GET  
Status Code: 200 OK  
Remote Address: 2607:f8b0:4006:2004::443  
Referrer Policy: strict-origin-when-cross-origin  

headers:  
:authority: www.google.com  
:method: GET  
:path: /  
:scheme: https  
accept: text/html  
sec-fetch-site: none  
sec-fetch-mode: navigate  
sec-fetch-user: ?1  
user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X)  

### response  
content-encoding: br  
content-length: 82262  
content-type: text/html; charset=ISO-8859-1  
date: [fecha]  
server: gws  

---

## metodos comunes http

- **GET**: pide data, por ej cargar una pag o ver info d una api  
- **POST**: manda data al server, x ej. cuando uno envia un form  
- **PUT**: actualiza algo completo, como cambiar perfil  
- **DELETE**: borra un recurso, ej. borrar comentario  

---

## codigos d estado http

- **200 OK**: todo bien, la pagina cargo  
- **301 Moved Permanently**: la url cambió, redirecciona  
- **400 Bad Request**: algo mal en lo q el cliente mandó  
- **401 Unauthorized**: no esta logueado o falta permiso  
- **404 Not Found**: no se encontro la pagina o recurso  
