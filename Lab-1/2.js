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
        const keyword = document.getElementById("keyword");
        //check keyword
        for (let i = 0; i < keyword.value.length; i ++){
            for (let j = i+1; j < keyword.value.length; j ++){
                if (keyword.value.charAt(i) == keyword.value.charAt(j)){
                    alert("input a valid keyword with no repeating letters");
                    return;
                }
            }

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


        const newKeyword = keyword.value.toUpperCase();
        // changing the alphabet
        let newAlphabet = [];
        for (let i = 0; i < newKeyword.length; i ++){
            newAlphabet[i] = newKeyword.charAt(i);
        }

        let letterToAdd = false;
        for (let i = 0; i < al.length; i ++){
            letterToAdd = true;
            for (let j = 0; j < newAlphabet.length; j++){
                if (al[i] == newAlphabet[j]){
                    letterToAdd = false;
                }
            }

            if (letterToAdd){
                newAlphabet[newAlphabet.length] = al[i];
            }
        }

        // encrypting the message
        newMessage = message.value.toUpperCase();
        let code = "";

        for (let i = 0; i < newMessage.length; i++) {
            for (let j = 0; j < newAlphabet.length; j++){
                if (newMessage.charAt(i) == newAlphabet[j]){
                    let newIndex = j + parseInt(key.value);
                    if (newIndex >= newAlphabet.length){
                        newIndex =  newIndex - newAlphabet.length ;
                    }
                    code = code.concat(newAlphabet[newIndex]);
                }
            }
          }

          cryptogram.value = code;
          
    })

if (cbutton)
    cbutton.addEventListener("click", function(event){
        event.preventDefault();
        const key = document.getElementById("key");
        const keyword = document.getElementById("keyword");
        const message = document.getElementById("message");
        const cryptogram = document.getElementById("cryptogram");

        key.value = null;
        keyword.value = null;
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

        const keyword = document.getElementById("keyword");
        //check keyword
        for (let i = 0; i < keyword.value.length; i ++){
            for (let j = i+1; j < keyword.value.length; j ++){
                if (keyword.value.charAt(i) == keyword.value.charAt(j)){
                    alert("input a valid keyword with no repeating letters");
                    return;
                }
            }

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

        const newKeyword = keyword.value.toUpperCase();
        // changing the alphabet
        let newAlphabet = [];
        for (let i = 0; i < newKeyword.length; i ++){
            newAlphabet[i] = newKeyword.charAt(i);
        }

        let letterToAdd = false;
        for (let i = 0; i < al.length; i ++){
            letterToAdd = true;
            for (let j = 0; j < newAlphabet.length; j++){
                if (al[i] == newAlphabet[j]){
                    letterToAdd = false;
                }
            }

            if (letterToAdd){
                newAlphabet[newAlphabet.length] = al[i];
            }
        }

        const newCrypt = cryptogram.value.toUpperCase();
        let decrypt = "";

        for (let i = 0; i <= newCrypt.length; i ++){
            for (let j = 0; j <= newAlphabet.length; j++){
                if (newCrypt.charAt(i) ==  newAlphabet[j]){
                    let newIndex = j - parseInt(key.value);
                    if (newIndex < 0){
                        newIndex = newAlphabet.length + newIndex;
                    }

                    decrypt = decrypt.concat(newAlphabet[newIndex]);
                }
            }
        }
        
        message.value = decrypt;
    })