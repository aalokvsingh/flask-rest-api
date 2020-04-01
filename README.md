# flask-rest-api
I will create Rest API in Python Flask framework that will use HTTP methods and mysql database
<br/>
Firstly you have make sure below thing ready installed before you code
<ol>
  <li>python3</li>
  <li>Visual Studio Code (<i>This editor make the coding easy by hints and linter. I prefer it.</i>)</li>
  <li>Python Modules</li>
  <ol>
    <li>flask</li>
    <li>flask_sqlalchemy (<i>orm for communication mysql</i>)</li>
    <li>jwt(<i>JSON Web Token</i>)</li>
    <li>werkzeug</li>
  </ol>
 </ol>
<br/>There are three flaour of api I have created
<ol>
  <li>api.py<br/>
    <i>This is simple api having json in a variable. you will come to know how to use route and method in flask while creating rest api</i>
  </li>
   <li>app.py<br/>
     <i>This REST api does not make use of databse, but you have idea of REST API functionality</i>
  </li>
   <li>main.py<br/>
     <i>This is full function rest api with user registration, login, token to access further apis like create post, list post, delete post etc. </i>
  </li>
 </ol>

<h3>I will show the main.py api using postman. If you dont have postman install it</h3>

login:
http://127.0.0.1:5000/login1
<code>
output: <br/>
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFsb2sxIiwiZXhwIjoxNTg1NzU1ODgxfQ.GYSChwIf8sg_65q4yfugeoZpbifn6js-fgnl3SZ1LCo"
}
</code>
<br/>
create post:<br/>
http://127.0.0.1:5000/createpost
<br/>In header put<br/>
x-access-tokens : eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFsb2sxIiwiZXhwIjoxNTg1NzU1ODgxfQ.GYSChwIf8sg_65q4yfugeoZpbifn6js-fgnl3SZ1LCo
<br/>
Content-Type : application/json
<br/>input:<br/>
<code>
{
"post_title":"title 113",
"post_content" : "content 113",
"post_time":"2020-03-30",
"filename":"alok11.txt",
"post_status":1
}
</code>
<br/>output:<br/>
<code>
  {
    "message": "new post created"
}
</code><br/>
<H3>I will make it more informative</h3>



