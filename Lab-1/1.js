const al = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];
const mi = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];

const form = document.getElementById("cForm");
const ebutton = document.getElementById("eButton");
const dbutton = document.getElementById("dButton");
const cbutton = document.getElementById("cButton");


if (ebutton)
    ebutton.addEventListener("click", function(event){
        event.preventDefault();

        const key = document.getElementById("key");
        //check key
        if (parseInt(key.value) < 1 || parseInt(key.value) > 25){
            alert("input a valid key range 1-25");
            return;        
        }
        const message = document.getElementById("message");
        let goodMessage = false;
        //check message
        for (let i = 0; i < message.value.length; i ++){
            goodMessage = false;
            for (let j = 0; j < al.length; j++){
                if (message.value.charAt(i) == al[j] || message.value.charAt(i) == mi[j]){
                        goodMessage = true;
                } 
            }
            if (!goodMessage){
                alert("input a valid message A-Z or a-z");
                return;
            }
        }
        const cryptogram = document.getElementById("cryptogram");
        if (cryptogram.value != ""){
            alert("leave the cryptogram field empty if you wish to encrypt");
            return;
        }

        newMessage = message.value.toUpperCase();
        let code = "";

        for (let i = 0; i < newMessage.length; i++) {
            for (let j = 0; j < al.length; j++){
                if (newMessage.charAt(i) == al[j]){
                    let newIndex = j + parseInt(key.value);
                    if (newIndex >= al.length){
                        newIndex =  newIndex - al.length ;
                    }
                    code = code.concat(al[newIndex]);
                }
            }
          }

          cryptogram.value = code;
          
    })
    
if (cbutton)
    cbutton.addEventListener("click", function(event){
        event.preventDefault();
        const key = document.getElementById("key");
        const message = document.getElementById("message");
        const cryptogram = document.getElementById("cryptogram");

        key.value = null;
        message.value = null;
        cryptogram.value = null;
    })

if (dbutton)
    dbutton.addEventListener("click", function(event){
        event.preventDefault();
        const key = document.getElementById("key");
        //check key
        if (parseInt(key.value) < 1 || parseInt(key.value) > 25){
            alert("input a valid key range 1-25");
            return;        
        }
        const message = document.getElementById("message");
        const cryptogram = document.getElementById("cryptogram");
        //check cryptogram
        for (let i = 0; i < cryptogram.value.length; i ++){
            goodMessage = false;
            for (let j = 0; j < al.length; j++){
                if (cryptogram.value.charAt(i) == al[j] || cryptogram.value.charAt(i) == mi[j]){
                        goodMessage = true;
                } 
            }
            if (!goodMessage){
                alert("input a valid cryptogram A-Z or a-z");
                return;
            }
        }
        const newCrypt = cryptogram.value.toUpperCase();
        console.log(newCrypt);
        let decrypt = "";

        for (let i = 0; i <= newCrypt.length; i ++){
            for (let j = 0; j <= al.length; j++){
                if (newCrypt.charAt(i) ==  al[j]){
                    let newIndex = j - parseInt(key.value);
                    if (newIndex < 0){
                        newIndex = al.length + newIndex;
                    }

                    decrypt = decrypt.concat(al[newIndex]);
                    // console.log(al[newIndex]);
                    // console.log(decrypt);
                }
            }
        }
        
        message.value = decrypt;
        console.log(decrypt);
    })