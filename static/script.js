console.log("Working")
function login(){

var username  = document.getElementById('name').value
var email = document.getElementById('email').value
var password = document.getElementById('password').value

if (username == "" || email  == "" || password == ""){
alert('You must enter every field');
}
var csrf = document.getElementById('csrf').value;

var data = {

'username' :username,
'email' : email,
"password" : password
}
fetch ('/api/login/' ,{
method : "POST",
headers :{
'Content-Type' : 'application/json',
"X-CSRFToken" : csrf
},
'body':JSON.stringify(data)

}).then(result => result.json())
.then(response =>{

if (response.status == 200){
window.location.href = "http://127.0.0.1:8000/blogs/home/";
}
else{
alert(response.message)
}


})

}
function register(){

var username  = document.getElementById('name').value
var email = document.getElementById('email').value
var password = document.getElementById('password').value

if (username == "" || email  == "" || password == ""){
alert('You must enter every field');
}
var csrf = document.getElementById('csrf').value;

var data = {

'username' :username,
'email' : email,
"password" : password
}
fetch ('/api/register/' ,{
method : "POST",
headers :{
'Content-Type' : 'application/json',
"X-CSRFToken" : csrf
},
'body':JSON.stringify(data)

}).then(result => result.json())
.then(response =>{

if (response.status == 200){
window.location.href = "http://127.0.0.1:8000/blogs/home/";
}
else{
alert(response.message)
}


})

}