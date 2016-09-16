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
    console.log(handleTextType);
}

function handleTextAreaType(){
    console.log(handleTextType);
}

function handleNumberType(){
    console.log(handleTextType);
}

function handleEmailType(){
    console.log(handleTextType);
}

function handlePasswordType(){
    console.log(handleTextType);
}

function handleDropdownType(){
    console.log(handleTextType);
}

function handleRadiosType(){
    console.log(handleTextType);
}

function handleRadiosInlineType(){
    console.log(handleTextType);
}

function handleRadioButtonsType(){
    console.log(handleTextType);
}

function handleCheckboxType(){
    console.log(handleTextType);
}

function handleCheckboxesType(){
    console.log(handleTextType);
}

function handleBooleanType(){
    console.log(handleTextType);
}

function handleDateType(){
    console.log(handleTextType);
}

function handleTimeType(){
    console.log(handleTextType);
}

function handleDateTimeType(){
    console.log(handleTextType);
}

function handleButtonType(){
    console.log(handleTextType);
}

function handleSubmitType(){
    console.log(handleTextType);
}

function handleResetType(){
    console.log(handleTextType);
}

function handleHelpType(){
    console.log(handleTextType);
}

function handleTemplateType(){
    console.log(handleTextType);
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
















