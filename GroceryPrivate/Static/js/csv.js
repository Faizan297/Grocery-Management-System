    $('#sname,#fname,#mname').on("keydown", function (e) {
    let ch = String.fromCharCode(e.which);
    let $error = $(this).closest('.col-12').find('.error-msg'); // only target error span
    $error.text(""); // clear old error
    exp=/^[A-Za-z\s\t\b\x14\x25-\x28]$/

    if (!(exp.test(ch))) {
      $error.text("Only alphabets and space allowed!").css({ "color": "red" });
      setTimeout(() => {
        $error.text("");
       }, 1000);
      
      
      return false;
     }
    else if (ch=="\x20" && (this.selectionStart===0 || $(this).val().slice(-1)===" "))
      return false;
    });

    
    $('#cont,#cont2').on("keydown",function(e){
      let ch=String.fromCharCode(e.which);
      let $error =$(this).closest('.col-12').find('.error-msg');
      $error.text("");
      exp=/^[\d\t\b\x0D\x2e\x25-\x28\x60-\x69]$/

      if(!(exp.test(ch))){
        $error.text("Only digits are allowed!").css({"color": "red"})
        setTimeout(() => {
        $error.text("");
       }, 1000);
      
        return false;


      }
    if (e.shiftKey) {
        $error.text("Special characters are not allowed!").css({ "color": "red" });
        e.preventDefault();
        setTimeout(() => {
        $error.text("");
       }, 1000);
      
        return false;
    }
    if ($(this).val().length === 0 && (ch === "\x30" || ch === "\x60")) {
      $error.text("Number cannot start with 0 !").css({ "color": "red" });
      setTimeout(() => {
        $error.text("");
       }, 1000);
      
      return false;
    }
      //  Prevent typing extra digits beyond 10
    if ($(this).val().length >= 10 && /^\d$/.test(e.key)) {
      $error.text("Max 10 digits are allowed!").css({ "color": "red" });
      setTimeout(() => {
        $error.text("");
       }, 1000);
      
      return false;
    }

    });
    //  for Aadhaaar -----------
  $('#aadhaar').on("keydown",function(e){
   let ch=String.fromCharCode(e.which)
   let $error = $(this).closest('.col-12').find('.error-msg');
   $error.text("");
   exp=/^[\d\t\b\x0D\x2e\x25-\x28\x60-\x69]$/

   if (!(exp.test(ch))){
    $error.text("Only digits are allowed!").css({"color":"red"});
    setTimeout(() => {
        $error.text("");
       }, 1000);
      
    return false;
   }
   else if ($(this).val().length === 0 && ch === "\x30" || ch === "\x60"){
    $error.text("Invalid !").css({"color": "red"});
    setTimeout(() => {
        $error.text("");
       }, 1000);
      
    return false;
   }
   else if (e.shiftKey){
      $error.text("Special characters are not Allowed !").css({"color":"red"});
      setTimeout(() => {
        $error.text("");
       }, 1000);
      
      return false;
   }
   else if ($(this).val().length >= 12 && /^\d$/.test(e.key)){
       $error.text("Max 12 digits are allowed !").css({"color":"red"})
       setTimeout(() => {
        $error.text("");
       }, 1000);
      
       return false;
   }
     
      
  });
  $('#salary,#pin1,#pin2,#disc,#pay,#tax').on("keydown" ,function(e){
    let ch=String.fromCharCode(e.which);
    let $error=$(this).closest('.col-12').find('.error-msg');
    $error.text("");
    exp=/^[\d\t\b\x0D\x2e\x25-\x28\x60-\x69]$/

    if (!(exp.test(ch))){
      $error.text("Only digits are allowed !").css({"color":"red"});
      setTimeout(() => {
        $error.text("");
       }, 1000);
      
      return false;
    }
    //  prevent special characgter enter with shift -------
    else if (e.shiftKey){
      $error.text("Invalid Format !").css({"color":"red"});
      setTimeout(() => {
        $error.text("");
       }, 1000);
      
      return false;
    }
    //  prevent starting with 0-------
    else if ($(this).val().length===0 && (ch === "\x30" || ch === "\x60")){  
      $error.text("Invalid !").css({"color":"red"});
      setTimeout(() => {
        $error.text("");
       }, 1000);
      
      return false;
    }
     //  prevent max digit 6 -------
    else if ($(this).val().length>=6 && /^\d$/.test(e.key)) {
      $error.text("Max 6 Digits are allowed !").css({"color":"red"})
      setTimeout(() => {
        $error.text("");
       }, 1000);
      
      return false;

    }

  });
   //  for category id with alphanumeric---------------------
   $('#category,#uid,#cid,#prid').on("keydown",function(e){
      let ch =String.fromCharCode(e.which);
      let $error=$(this).closest('.col-12').find('.error-msg');
      $error.text("");
      exp=/^[A-Za-z\d\t\b\x0D\x2e\x25-\x28\x60-\x69]$/

      if (!(exp.test(ch))){
        $error.text("Invalid Format !").css({"color":"red"});
        setTimeout(() => {
        $error.text("");
       }, 1000);
      
        return false;
      }
      else if(e.shiftKey){
        $error.text("Invalid Format !").css({"color":"red"});
        setTimeout(() => {
        $error.text("");
       }, 1000);
      
        return false;
      }
      else if ($(this).val().length >=16 && /^[A-Za-z\d]$/.test(e.key)){
        $error.text("Max 16 Digits are allowed !").css({"color":"red"})
        setTimeout(() => {
        $error.text("");
       }, 1000);
      
        return false;

      }
   });
 // extraaaa part( for user id etc...)------------------
  $('#user,#order,#purchase').on("keydown",function(e){
   let ch = String.fromCharCode(e.which);
   let $error= $(this).closest('.col-12').find('.error-msg');
   $error.text("");
   exp=/^[\d\t\b\x0D\x2e\x25-\x28\x60-\x69]$/
   if (!(exp.test(ch))){
    $error.text("Only digits are allowed !").css({"color":"red"});
    setTimeout(() => {
        $error.text("");
       }, 1000);
      
    return false;
   }
   else if(e.shiftKey){
    $error.text("Invalid Format !").css({"color":"red"});
    setTimeout(() => {
        $error.text("");
       }, 1000);
      
    return false;
   }
   else if ($(this).val().length>=16 && /^\d$/.test(e.key)){
    $error.text("Max 16 digits are allowed !").css({"color":"red"})
    setTimeout(() => {
        $error.text("");
       }, 1000);
      
    return false;
   }
  });
    //   //  for GST Number//
    $('#gst').on("keydown",function(e){
     let ch=String.fromCharCode(e.which);
     let $error=$(this).closest('.col-12').find('.error-msg');
     $error.text("");
     L=$('#gst').val().length;
     exp=/^[\d\t\x0D\b\x2e\x25-\x28\x60-\x69]$/
     if(L==15 && ch!="\b" && ch!="\t" && ch!="\x0D")
      { 
          $error.text("Maximum 15 characters are allowed !").css({ "color": "red" });
          setTimeout(() => {
        $error.text("");
       }, 1200);
      
          return false;
      }    
     else if((L>=0 && L<2)|| L==14){
       if(!(exp.test(ch))){
        if(L==14){
          $error.text("Last Character must be Digit !").css({"color":"red"});
          setTimeout(() => {
        $error.text("");
       }, 1200);
       
          }
        else {
           $error.text(" First two characters must be Digit !").css({"color":"red"});
           setTimeout(() => {
        $error.text("");
       }, 1200);
      
           }
           return false;
         }
       else if(e.shiftKey){
          $error.text("Invalid Format !").css({"color":"red"});
          setTimeout(() => {
        $error.text("");
       }, 1200);
      
          return false;
        }
      }
     else if(L>=2 && L<7){
        exp1=/^[A-za-z\b\t\x2e\x25-\x28]$/

       if(!(exp1.test(ch))){
         $error.text("Five characters must be Alphabet !").css({ "color": "red" });
         setTimeout(() => {
        $error.text("");
       }, 1200);
      
         return false;
      }
      }
       
     else if(L>=7 && L<11){
      exp2=/^[\d\t\b\x2e\x25-\x28\x60-\x69]$/
       if(!(exp2.test(ch))){
          $error.text("Four characters must be Digit !").css({ "color": "red" });
          setTimeout(() => {
        $error.text("");
       }, 1200);
      
          return false;
         }
       else if(e.shiftKey){
          $error.text("Special charachters are not allowed !").css({"color":"red"});
          setTimeout(() => {
        $error.text("");
       }, 1200);
      
          return false;
        }
          }
      
     
     else if(L==11){
      exp3=/^[A-Z\t\b\x2e\x25-\x28]$/
      if(!(exp3.test(ch))){
        $error.text("One characters must be Alphabet !").css({ "color": "red" });
        setTimeout(() => {
        $error.text("");
       }, 1200);
      
        return false;
      }
     }
     else if(L==12){
      exp4=/^[\d\t\b\x2e\x25-\x28\x60-\x69]$/
      if(!(exp4.test(ch))){
        $error.text("One characters must be Digit !").css({ "color": "red" });
        setTimeout(() => {
        $error.text("");
       }, 1200);
      
        return false;
      }
      else if(e.shiftKey){
          $error.text("Special charachters are not allowed !").css({"color":"red"});
          setTimeout(() => {
        $error.text("");
       }, 1200);
      
          return false;
        }
     }
     
     else if(L==13){
      exp5=/^[\x5a\t\b\x2e\x25-\x28]$/
      if(!(exp5.test(ch))){
        $error.text("Character must be Z !").css({ "color": "red" });
        setTimeout(() => {
        $error.text("");
       }, 1200);
      
        return false;
      }
     }
     
   
    });
    
// $('#gst').on('input', function () {
//   let $error = $(this).closest('.col-12').find('.error-msg');
//   let val = this.value.toUpperCase();

//   // Allow only A–Z and 0–9
//   val = val.replace(/[^A-Z0-9]/g, '');

//   // Enforce max length
//   if (val.length > 15) {
//     val = val.slice(0, 15);
//   }

//   // Position-based rules
//   const rules = [
//     /^[0-9]{0,2}$/,                                   // 0–1
//     /^[0-9]{2}[A-Z]{0,5}$/,                           // 2–6
//     /^[0-9]{2}[A-Z]{5}[0-9]{0,4}$/,                   // 7–10
//     /^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]?$/,               // 11
//     /^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][0-9]?$/,          // 12
//     /^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][0-9]Z?$/,         // 13
//     /^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][0-9]Z[0-9]?$/
//   ];

//   const validSoFar = rules.some(r => r.test(val));

//   if (!validSoFar) {
//     // Remove last character
//     val = val.slice(0, -1);
//     $error.text("Invalid GST format").css("color", "red");
//   } else {
//     $error.text("");
//   }

//   this.value = val;
// });


//     // for show-hide animation
    $(document).ready(function(){
    $("#search-show").click(function(){
      $("#search-hide").slideToggle();
    })
  });

  //   //  $("#submit1,#submit2").on("click",function(e){
//   //   e.preventDefault();
  
//   //    p=["#sname","#fname","#mname","#cont","#cont2","#aadhaar","#qualification","#salary","#pin1","#pin2"
//   //     , "#email1","#disc","#pay","#tax","#category","#user","#order" ,"#position1","#status1","#state1","#district1","#photo3", "#aadhaar3","#signature3","#certificate3" ,"#purchase" ,"#gst" ,"#category","#uid","#cid","#prid"];
//   //    for ( i in p)
//   //    { 
//   //     let v=$(p[i]).val()
//   //     if (v != undefined ){
//   //       if(v.length==0)
//   //        { 
//   //          if ( i != 17 && i != 18 && i != 19 &&  i != 20 && i != 21 && i != 22 && i != 23 && i != 24) {
//   //            $(p[i]).val("Field is mandatory*");
//   //          }
//   //          $(p[i]).css({ "border": "2px solid red", "color": "red" });
//   //        }
//   //       else if ($('#cont,#cont2').val().length!==10){
//   //            $('#cont,#cont2').val("Contact should be 10 digits*");
//   //            $('#cont,#cont2').css({ "border": "2px solid red", "color": "red" });
        
//   //         }

//   //     }
//   //   }

//   //  author----------
//   $("#sign_up1").on("click",function(e){
//     e.preventDefault(); 
//     p=["#sname","#fname","#mname","#cont","#cont2","#aadhaar","#qualification","#salary","#pin1","#pin2"
//         , "#email1","#disc","#pay","#tax","#category","#user","#order" ,"#position1","#status1","#state1","#district1","#photo3", "#aadhaar3","#signature3","#certificate3" ,"#purchase" ,"#gst" ,"#category","#uid","#cid","#prid"];
//     for ( i in p)
//     { 
//       let v=$(p[i]).val()
//       if (v != undefined ){
//         if(v.length==0)
//         { 
//           if ( i != 17 && i != 18 && i != 19 &&  i != 20 && i != 21 && i != 22 && i != 23 && i != 24) {
//             $(p[i]).val("Field is mandatory*");
//           }
//           $(p[i]).css({ "border": "2px solid red", "color": "red" });
//       }
//     }
//   }

//     });

    // stop auto fill
    // $("input[type=text]").attr("autocomplete", "new-password");
