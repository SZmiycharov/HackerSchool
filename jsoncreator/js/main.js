function getParameterByName(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}    

var title = getParameterByName('title');
var type = getParameterByName('type');
var key = getParameterByName('key');
var description = getParameterByName('description');
var hidetitle = getParameterByName('hidetitle');
var disablesuccess = getParameterByName('disablesuccess');
var disableerror = getParameterByName('disableerror');
var readonly = getParameterByName('readonly');
var validationmessage = getParameterByName('validationmessage');
var onchange = getParameterByName('onchange');
var feedbackicon = getParameterByName('feedbackicon');
var placeholder = getParameterByName('placeholder');
var ngmodeloptions = getParameterByName('ngmodeloptions');
var classoffield = getParameterByName('classoffield');
var destroystrategy = getParameterByName('destroystrategy');
var copyvalueto = getParameterByName('copyvalueto');
var fieldclass = getParameterByName('fieldclass');
var labelclass = getParameterByName('labelclass');
var condition = getParameterByName('condition');
var fieldaddonleft = getParameterByName('fieldaddonleft');
var fieldaddonright = getParameterByName('fieldaddonright');


function showAdvancedOptions(){
        if(document.getElementById('showadvancedoptions').checked) {
            $("#advancedoptions").show();
        } else {
            $("#advancedoptions").hide();
        }
};

function handleTextType(){
    console.log('1');
    var element = document.getElementById("p1");
    element.innerHTML = "New text!";
}

function handleTextAreaType(){
    console.log('2');
    var element = document.getElementById("p1");
    element.innerHTML = "New text!";
}

function handleNumberType(){
    console.log('3');
    var element = document.getElementById("p1");
    element.innerHTML = "New text!";
}

function handleEmailType(){
    console.log('4');
    var element = document.getElementById("p1");
    element.innerHTML = "New text!";
}

function handlePasswordType(){
    console.log('5');
    var element = document.getElementById("p1");
    element.innerHTML = "New text!";
}

function handleDropdownType(){
    console.log('6');
    var element = document.getElementById("p1");
    element.innerHTML = "New text!";
}

function handleRadiosType(){
    console.log('7');
    var element = document.getElementById("p1");
    element.innerHTML = "New text!";
}

function handleRadiosInlineType(){
    console.log('8');
    var element = document.getElementById("p1");
    element.innerHTML = "New text!";
}

function handleRadioButtonsType(){
    console.log('9');
    var element = document.getElementById("p1");
    element.innerHTML = "New text!";
}

function handleCheckboxType(){
    console.log('10');
    var element = document.getElementById("p1");
    element.innerHTML = "New text!";
}

function handleCheckboxesType(){
    console.log('11');
    var element = document.getElementById("p1");
    element.innerHTML = "New text!";
}

function handleBooleanType(){
    console.log('12');
    var element = document.getElementById("p1");
    element.innerHTML = "New text!";
}

function handleDateType(){
    console.log('13');
    var element = document.getElementById("p1");
    element.innerHTML = "New text!";
}

function handleTimeType(){
    console.log('14');
    var element = document.getElementById("p1");
    element.innerHTML = "New text!";
}

function handleDateTimeType(){
    console.log('15');
    var element = document.getElementById("p1");
    element.innerHTML = "New text!";
}

function handleButtonType(){
    console.log('16');
    var element = document.getElementById("p1");
    element.innerHTML = "New text!";
}

function handleSubmitType(){
    console.log('17');
    var element = document.getElementById("p1");
    element.innerHTML = "New text!";
}

function handleResetType(){
    console.log('18');
    var element = document.getElementById("p1");
    element.innerHTML = "New text!";
}

function handleHelpType(){
    console.log('19');
    var element = document.getElementById("p1");
    element.innerHTML = "New text!";
}

function handleTemplateType(){
    console.log('20');
    var element = document.getElementById("p1");
    element.innerHTML = "New text!";
}

switch(type){
    case 'text':
        handleTextType(); break;
    case 'textarea':
        handleTextAreaType(); break;
    case 'number':
        handleNumberType(); break;
    case 'email':
        handleEmailType(); break;
    case 'password':
        handlePasswordType(); break;
    case 'dropdown':
        handleDropdownType(); break;
    case 'radios':
        handleRadiosType(); break;
    case 'radios-inline':
        handleRadiosInlineType(); break;
    case 'radiobuttons':
        handleRadioButtonsType(); break;
    case 'checkbox':
        handleCheckboxType(); break;
    case 'checkboxes':
        handleCheckboxesType(); break;
    case 'boolean':
        handleBooleanType(); break;
    case 'date':
        handleDateType(); break;
    case 'time':
        handleTimeType(); break;
    case 'date-time':
        handleDateTimeType(); break;
    case 'button':
        handleButtonType(); break;
    case 'submit':
        handleSubmitType(); break;
    case 'reset':
        handleResetType(); break;
    case 'help':
        handleHelpType(); break;
    case 'template':
        handleTemplateType(); break;       
}
















