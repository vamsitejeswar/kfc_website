var mybutton=document.getElementById("mybtn");
window.onscroll=function(){scrollfunction()};
function scrollfunction(){
    if (document.body.scrollTop>100||document.documentElement.scrollTop>100){
        mybutton.style.display="block";
        }
    else{
        mybutton.style.display="none";
        }
    }
function topfunction(){
    document.body.scrollTop=0;
    document.documentElement.scrollTop=0;
}
// owl carousel in index page
$('.owl-carousel').owlCarousel({
  loop:true,
  margin:10,
  responsiveClass:true,
  responsive:{
      0:{
          items:2,
        //   nav:true
      },
      501:{
          items:3,
        //   nav:true
      },
      1000:{
          items:4,
        //   nav:true,
          loop:false
      }
  }
})
// login in login page
function validate(){
  var user=document.getElementById('user').value;
  var num=document.getElementById('num').value;
  var emails=document.getElementById('emails').value;
  var pass=document.getElementById('pass').value;
  var confirmpass=document.getElementById('conpass').value;

  //user
  if (user==""){
      document.getElementById('username').innerHTML="**please fill the username field";
      return false;
  }
  if ((user.length<=2) || (user.length>20)){
      document.getElementById('username').innerHTML="**username length must be b/w 2 and 20";
      return false;
  }
  if (!isNaN(user)){
      document.getElementById('username').innerHTML="**only characters we allowed";
      return false;
  }
  //mobile number
  if (num==""){
    document.getElementById("mnum").innerHTML="**please fill the mobile number field";
    return false
  }
  if (isNaN(num)){
    document.getElementById("mnum").innerHTML="**user must write digits only not characters";
    return false;
  }
  if (num.length!=10){
    document.getElementById("mnum").innerHTML="** mobile number must conatin 10 digits only";
    return false
  }
  //for email
  if (emails==""){
      document.getElementById('emailids').innerHTML="**please fill the mail id field";
      return false;
  }
  if(emails.indexOf('@')<=0){
      document.getElementById('emailids').innerHTML="**must include '@'";
      return false;
  }
  if ((emails.charAt(emails.length-4)!='.')&&(emails.charAt(emails.length-3)!='.')){
      document.getElementById('emailids').innerHTML="** .Invalid position";
      return false;
  }
  //password
  if (pass == ""){
      document.getElementById("password").innerHTML="**please fill the password field";
      return false;
  }
  if ((pass.length <=5 ) || (pass.length > 20)){
      document.getElementById("password").innerHTML="**password length must be b/w 5 and 20";
      return false;
  }
  //confirmpassword
  if (pass != confirmpass){
    document.getElementById("confirmpass").innerHTML="**password does not match the confirm password";
    return false;
  }
}


