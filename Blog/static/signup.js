let fieldset1 = document.getElementById('fieldset1')
let fieldset2 = document.getElementById('fieldset2')
let fieldset3 = document.getElementById('fieldset3')

let back1 = document.querySelector('#back1')
let back2 = document.querySelector('#back2')

let continue1 = document.querySelector('#continue1')
let continue2 = document.querySelector('#continue2')

continue2.onclick = function(){
    fieldset2.style.left = '40px';
    fieldset1.style.left = '-500px';
}

continue1.onclick = function(){
    fieldset3.style.left = '50px';
    fieldset2.style.left = '-500px';
}

back2.onclick = function(){
    fieldset2.style.left = '40px';
    fieldset3.style.left = '500px';
}

back1.onclick = function(){
    fieldset1.style.left = '50px';
    fieldset2.style.left = '500px';
}

                                                    //  fieldset inputs

let fieldset1_inputs, fieldset2_inputs, fieldset3_inputs

let fieldsets = [fieldset1, fieldset2, fieldset3]

fieldsets.forEach(fieldset =>{
    fieldset1_inputs = fieldset.querySelectorAll('input')
})
