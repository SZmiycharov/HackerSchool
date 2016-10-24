(function svzMainFunction ($) {
      'use strict';
        $( document ).ready(function() {
          window.onerror = function (msg, url, lineNo, columnNo, error) {
            var string = msg.toLowerCase();
            var substring = "script error";
            if (string.indexOf(substring) > -1){
                console.log('Script Error: See Browser Console for Detail');
            } else {
                var message = [
                    'Message: ' + msg,
                    'URL: ' + url,
                    'Line: ' + lineNo,
                    'Column: ' + columnNo,
                    'Error object: ' + JSON.stringify(error)
                ].join(' - ');

                console.log(message);
            }
            return false;
          };

          var TIMEOUT_DEBOUNCE = 500;
          
          var currentSchemaFormID = 1;
          var currentContainerID = 5;
          var currentItemID = 5;
          var allKeys = [];
          var jsonPreview = {};

          var editor = ace.edit('svz-json-text');
          editor.getSession().setMode('deps/javascript');
          editor.$blockScrolling = Infinity;

          editor.setOptions({
              enableBasicAutocompletion: true,
              enableLiveAutocompletion: true
          });


          jQuery.fn.extend({
            prependClass: function(newClasses) {
                return this.each(function() {
                    var currentClasses = $(this).prop("class");
                    $(this).removeClass(currentClasses).addClass(newClasses + " " + currentClasses);
                });
            }
          });

          var GetAllPaths = function(obj, prefix){
              var keys = Object.keys(obj);
              prefix = prefix ? prefix + '.' : '';
              return keys.reduce(function(result, key){
                  if(typeof obj[key] === 'object'){
                      result = result.concat(GetAllPaths(obj[key], prefix + key));
                  }else{
                      result.push(prefix + key);
                  }
                  return result;
              }, []);
          };

          var draggedObject;
          var propertiesBeforeStart;
          var stopToReturn;
          var pathToDelete;
          var keyToDelete;

          window.InitializeSortable = function() {
            $('.container').sortable({
                delay: 150,
                items: '.item, .container-wrapper',
                cancel: ':button, input',
                axis: 'y',
                cursor: 'move',
                tolerance: 'pointer',
                connectWith: '.container',
                start: function(event, ui){
                  stopToReturn = false;
                  pathToDelete = '';
                  keyToDelete = '';
                  propertiesBeforeStart = properties;
                  var currentKeyItem = $('#' + ui.item.attr('id')).find('label').html();
                  var currentKeyContainer = $('#' + ui.item.attr('id')).parent().find('label').html(); 
                  if ($('#' + ui.item.attr('id')).parent().attr('id') !== 'svz-container1'){
                    var allPaths = GetAllPaths(properties);
                    for (var i = 0; i < allPaths.length; i++){
                      if (_.include(allPaths[i], currentKeyItem)){
                        var currentPath = allPaths[i].split('.' + currentKeyItem + '.type')[0];
                        break;
                      } else if ((_.include(allPaths[i], currentKeyContainer + '.')) 
                        && (currentKeyItem.replace(/[0-9]/g, '') === 'SVZlabel')
                        && (_.include(allPaths[i], 'items'))){
                        stopToReturn = true;
                      }
                    }
                    try{
                      if(Object.byString(properties, currentPath) === 'array'){
                        stopToReturn = true;
                      }
                    } catch(e){}

                    if (!stopToReturn){
                      draggedObject = Object.byString(properties, currentPath)[currentKeyItem];
                      // delete Object.byString(properties, currentPath)[currentKeyItem];
                      pathToDelete = currentPath;
                    }
                  } else{
                    if (properties[currentKeyItem]['type'] === 'array'){
                      stopToReturn = true;
                    }

                    draggedObject = properties[currentKeyItem];
                    // delete properties[currentKeyItem];
                  }
                  keyToDelete = currentKeyItem;
                },
                stop: function(event, ui) {
                  if (stopToReturn){
                    $(this).sortable('cancel');
                    return false;
                  }

                  var currentKeyItem = $('#' + ui.item.attr('id')).find('label').html();
                  var currentKeyContainer = $('#' + ui.item.attr('id')).parent().find('label').html(); 
                  
                  if ($('#' + ui.item.attr('id')).parent().attr('id') !== 'svz-container1'){
                    var allPaths = GetAllPaths(properties);
                    for (var i = 0; i < allPaths.length; i++){
                      if (_.include(allPaths[i], currentKeyContainer)){
                        var currentPath = allPaths[i].split('.type')[0];
                        break;
                      }
                    }
                    if(Object.byString(properties, currentPath)['type'] === 'array'){
                      $(this).sortable('cancel');
                      return false;
                    }
                    try{
                      if(pathToDelete){
                        delete Object.byString(properties, pathToDelete)[keyToDelete];
                      } else{
                        delete properties[keyToDelete];
                      }
                      Object.byString(properties, currentPath)['properties'][currentKeyItem] = draggedObject;
                    } catch(e){
                      if(pathToDelete){
                        delete Object.byString(properties, pathToDelete)[keyToDelete];
                      } else{
                        delete properties[keyToDelete];
                      }
                      //currentPath = currentPath.split('.').slice(0, -1).join('.');
                      Object.byString(properties, currentPath)[currentKeyItem] = draggedObject;
                    }
                  } else{
                    if(pathToDelete){
                      delete Object.byString(properties, pathToDelete)[keyToDelete];
                    } else{
                      delete properties[keyToDelete];
                    }
                    properties[currentKeyItem] = draggedObject;
                  }                  
                },
              });
          }

          window.InitializeMultiselectAndTagit = function(currentID) {
            $('#svz-selected-type' + currentID).multiselect({
              buttonWidth: '40%',
              nonSelectedText: 'Choose type',
              numberDisplayed: 3
            });
            $('#svz-enum' + currentID).tagit({
                allowSpaces: true,
                placeholderText: 'Enum',
            });
          }
    
          $(document).on('click', '.container, .item, .svz-label-item, .svz-label-container', function(e){
            if (e.target != this || $(this).attr('id') === 'svz-container1') return;
            e.stopPropagation();
            var currentID = $(this).attr('id').replace( /^\D+/g, '')

            if (_.include($(this).attr('id'), 'label')){
              if ($(this).attr('id') != 'svz-container1'){
                $(this).next().toggle();
              }
            } else{
              $('#' + $(this).find('.tab-content').attr('id')).toggle();
            }
          });

          $(document).on('click', '.svz-add-options-button', function(){
            var currentID = $(this).attr('id').replace( /^\D+/g, '');
            $('#svz-add-options-cont' + currentID).slideToggle();
          });

          $(document).on('mouseover', '.container', function(e){
            e.stopPropagation();
            if ($(this).attr('id') != 'svz-container1'){
              $(this).css('background-color', '#616a6b');
            }
          });
          $(document).on('mouseout', '.container', function(){
            if ($(this).attr('id') != 'svz-container1'){
              $(this).css('background-color', '#97a8a9');
            }
          });
          $(document).on('mouseover', '.item', function(e){
            e.stopPropagation();
            $(this).prependClass('currentItemHover');
          });
          $(document).on('mouseout', '.item', function(){
            $(this).removeClass('currentItemHover');
          });

          $(document).on('click', '#svz-sorting-btn', function(){
            if($(this).text() === 'Allow sorting'){
              InitializeSortable();
              $('.container').sortable('enable');

              $(this).text('Disallow sorting');
              $(this).attr('class', 'btn btn-danger');
            } else{
              $(this).text('Allow sorting');

              $(this).attr('class', 'btn btn-primary');
              $('.container').sortable('disable');
            }
          });

          window.AppendObjectArrayForm = function(currentID, currentType) {
            currentContainerID += 1;
            currentItemID += 1;
            var currentLabel = $('#svz-label-item' + currentID).html();
            $('svz-item-container' + currentLabel).parent().find('label');
            var parentID = $('#svz-item-container' + currentID).parent().attr('id');

            // try{
            //   if($('#svz-selected-type' + parentID.replace( /^\D+/g, '')).val().length === 1 
            //   && $('#svz-selected-type' + parentID.replace( /^\D+/g, '')).val()[0] === 'array'){
            //     return;
            //   }
            // } catch(e) {}
            
            var $submittedFormDiv = $('#tab-content' + currentID);

            $submittedFormDiv.find('.multiselect').remove();
            $submittedFormDiv.find('.ui-widget-content:last').remove();

            $('#svz-item-container' + currentID).replaceWith('<div class="container-wrapper" id="svz-cont-wrapper' + currentContainerID + '"><div class="container" id="svz-container' + currentContainerID + '"><div class="btn-group" role="group"><button id="svz-add-item' + currentContainerID + '" class="btn btn-secondary svz-add-item" type="button">+</button><button id="svz-remove-container' + currentContainerID + '" class="btn btn-secondary svz-remove-container" type="button" >-</button></div><label class="svz-label-container" id="svz-label-container' + currentContainerID + '">' + currentLabel + '</label></div></div></div>');
            
            $submittedFormDiv.find('[id]').each(function() { 
              var newID = $(this).attr('id').replace(/\d+$/, function(str) { return currentContainerID; });
              $(this).attr('id', newID);
            });
            $submittedFormDiv.find('[name]').each(function() { 
              var newID = $(this).attr('name').replace(/\d+$/, function(str) { return currentContainerID; });
              $(this).attr('name', newID);
            });

            $('#svz-container' + currentContainerID).append($submittedFormDiv.hide());

            $('#svz-container' + currentContainerID).append('<div class="item"  id="svz-item-container' + currentItemID + '"><div class="btn-group" role="group"><button  id="svz-add-container' + currentItemID +'" class="btn btn-secondary svz-add-container" type="button" style="display: none;">+</button> <button id="svz-remove-item' + currentItemID + '" class="btn btn-secondary svz-remove-item" type="button">-</button></div><label class="svz-label-item" id="svz-label-item' + currentItemID + '">New schema</label></div></div>');

            if ($('#svz-sorting-btn').text() === 'Disallow sorting'){
              InitializeSortable();
            }

            if (currentType == 'object'){
              var $clonedDiv = $('#tab-content9999999').clone();
              var currentDataTargetForm = $clonedDiv.find('.svz-form-tab').attr('data-target');
              $clonedDiv.find('.svz-form-tab').attr('data-target', currentDataTargetForm.replace(/[0-9]/g, '') + currentItemID);
              var currentDataTargetForm = $clonedDiv.find('.svz-schema-tab').attr('data-target');
              $clonedDiv.find('.svz-schema-tab').attr('data-target', currentDataTargetForm.replace(/[0-9]/g, '') + currentItemID);

              $clonedDiv.find('.multiselect').remove();
              $clonedDiv.find('.ui-widget-content:last').remove();
              $clonedDiv.find('[id]').each(function() { 
                var newID = $(this).attr('id').replace(/\d+$/, function(str) { return currentItemID; });
                $(this).attr('id', newID);
              });
              $clonedDiv.find('[name]').each(function() { 
                var newID = $(this).attr('name').replace(/\d+$/, function(str) { return currentItemID; });
                $(this).attr('name', newID);
              });
              var idWithoutNumber = $clonedDiv.attr('id').replace(/[0-9]/g, '');
              $clonedDiv.attr('id', idWithoutNumber + currentItemID);

            } else if (currentType == 'array'){
              var $clonedDiv = $('#tab-content9999998').clone();
              var currentDataTargetForm = $clonedDiv.find('.svz-form-tab').attr('data-target');
              $clonedDiv.find('.svz-form-tab').attr('data-target', currentDataTargetForm.replace(/[0-9]/g, '') + currentItemID);
              var currentDataTargetForm = $clonedDiv.find('.svz-schema-tab').attr('data-target');
              $clonedDiv.find('.svz-schema-tab').attr('data-target', currentDataTargetForm.replace(/[0-9]/g, '') + currentItemID);

              $clonedDiv.find('.multiselect').remove();
              $clonedDiv.find('.ui-widget-content:last').remove();
              $clonedDiv.find('[id]').each(function() { 
                var newID = $(this).attr('id').replace(/\d+$/, function(str) { return currentItemID; });
                $(this).attr('id', newID);
              });
              $clonedDiv.find('[name]').each(function() { 
                var newID = $(this).attr('name').replace(/\d+$/, function(str) { return currentItemID; });
                $(this).attr('name', newID);
              });
              var idWithoutNumber = $clonedDiv.attr('id').replace(/[0-9]/g, '');
              $clonedDiv.attr('id', idWithoutNumber + currentItemID);
              $clonedDiv.remove();
            }

            $('#svz-item-container' + currentItemID).append($clonedDiv);

            if ($('#svz-sorting-btn').text() === 'Disallow sorting'){
              InitializeSortable();
            }

            InitializeMultiselectAndTagit(currentContainerID);
            InitializeMultiselectAndTagit(currentItemID);
          }

          $(document).on('click', '.svz-add-item', function(e){
            e.stopPropagation();

            currentItemID += 1;
            var currentID = $(this).attr('id').replace( /^\D+/g, '');

            var $clonedDiv = $('#tab-content9999999').clone();
            var currentDataTargetForm = $clonedDiv.find('.svz-form-tab').attr('data-target');
            $clonedDiv.find('.svz-form-tab').attr('data-target', currentDataTargetForm.replace(/[0-9]/g, '') + currentItemID);
            var currentDataTargetForm = $clonedDiv.find('.svz-schema-tab').attr('data-target');
            $clonedDiv.find('.svz-schema-tab').attr('data-target', currentDataTargetForm.replace(/[0-9]/g, '') + currentItemID);

            $clonedDiv.find('.multiselect').remove();
            $clonedDiv.find('.ui-widget-content:last').remove();
            $clonedDiv.find('[id]').each(function() { 
              var newID = $(this).attr('id').replace(/\d+$/, function(str) { return currentItemID; });
              $(this).attr('id', newID);
            });
            $clonedDiv.find('[name]').each(function() { 
              var newID = $(this).attr('name').replace(/\d+$/, function(str) { return currentItemID; });
              $(this).attr('name', newID);
            });
            var idWithoutNumber = $clonedDiv.attr('id').replace(/[0-9]/g, '');
            $clonedDiv.attr('id', idWithoutNumber + currentItemID);

            if (!$(this).parent().parent().find('.container').html()){
              $('#svz-container' + currentID).append('<div class="item"  id="svz-item-container' + currentItemID + '"><div class="btn-group" role="group"><button id="svz-remove-item' + currentItemID + '" class="btn btn-secondary svz-remove-item" type="button">-</button></div><label class="svz-label-item" id="svz-label-item' + currentItemID + '">New schema</label></div>');
            } else {
              $('<div class="item"  id="svz-item-container' + currentItemID + '"><div class="btn-group" role="group"><button id="svz-remove-item' + currentItemID + '" class="btn btn-secondary svz-remove-item" type="button">-</button></div><label class="svz-label-item" id="svz-label-item' + currentItemID + '">New schema</label></div>').insertBefore('#svz-add-item' + currentID);
            }
            $('#svz-item-container' + currentItemID).append($clonedDiv);

            if ($('#svz-sorting-btn').text() === 'Disallow sorting'){
              InitializeSortable();
            }
            InitializeMultiselectAndTagit(currentItemID);
          });

          $(document).on('click', '.svz-remove-item', function(){
            delete properties[$(this).parent().parent().find('.svz-label-item').html()];
            allKeys.splice(_.indexOf(allKeys, $(this).parent().parent().find('.svz-label-item').html()), 1);
            $(this).parent().parent().remove();
            $(this).parent().remove();
          });

          $(document).on('click', '.svz-remove-container', function(){
            delete properties[$(this).parent().parent().find('.svz-label-container').html()];
            allKeys.splice(_.indexOf(allKeys, $(this).parent().parent().find('.svz-label-container').html()), 1);
            $(this).parent().parent().remove();
            $(this).parent().remove();
          });
          
          $(document).on('keyup', '.svz-key', function() {
             var currentID = $(this).attr('id').replace( /^\D+/g, '');

             if (_.include(allKeys, $(this).val()) 
              && $(this).val() != $('#svz-label-item' + currentID).html() 
              && $(this).val() != $('#svz-label-container' + currentID).html()){
                $('#svz-schema-form-submit' + currentID).prop('disabled', true);
                $('#svz-key-warning' + currentID).show();
                $('#svz-key' + currentID).css('border-color', '#ff0000');
              } else{
                $('#svz-schema-form-submit' + currentID).prop('disabled', false);
                $('#svz-key-warning' + currentID).hide();
                $('#svz-key' + currentID).css('border-color', '#cccccc');
              }
          });

          window.AppendInputFieldToForm = function(currentIDnum, label, ID, name, currentClass){
            $('#svz-schema-form' + currentIDnum).append('<div class="form-group additionaloption' + currentIDnum + '"><label class="additionaloption' + currentIDnum + '">' + label + '</label><input id="' + ID + currentIDnum + '" type="number" class="form-control ' + currentClass + '" name="' + name + currentIDnum + '" placeholder="' + label + '"></div>');
          }
          window.AppendCheckboxFieldToForm = function(currentIDnum, label, placeholder, IDdiv, IDinput, name){
            $('#svz-schema-form' + currentIDnum).append('<div hidden class="additionaloption' + currentIDnum + '" class="form-group"  id="' + IDdiv + currentIDnum + '"><label style="display: flex;"><input id="'+ IDinput + currentIDnum + '" name="' + name + currentIDnum + '" type="checkbox" placeholder="' + placeholder + '">' + label + '</label></div>');
          }
          window.AppendCheckboxFieldArray = function(currentIDnum){
            $('#svz-schema-form' + currentIDnum).append('<div class="additionaloption' + currentIDnum + '"><label style="display: flex;"><input id="svz-unique-items' + currentIDnum + '" name="uniqueItems' + currentIDnum + '" type="checkbox">Unique items (check for true)</label></div>');
          }
          window.AppendSubmitBtnToForm = function(currentIDnum){
            $('#svz-schema-form' + currentIDnum).append('<input class="btn btn-default" id="svz-schema-form-submit' + currentIDnum + '" type="submit" value="Update">');
          }
          window.AppendReadonlyFieldToForm = function(currentIDnum){
            $('#svz-schema-form' + currentIDnum).append('<div class="additionaloption' + currentIDnum + '"><label style="display: flex;"><input id="svz-readonly' + currentIDnum + '" name="readonly' + currentIDnum + '" type="checkbox">Readonly (check for true)</label></div>');
          }

          window.RemoveFormShowEnum = function(currentIDnum){
            $('#svz-schema-form-submit' + currentIDnum).remove();
            $('#svz-enum' + currentIDnum).show();
            $('#svz-enum').prop('disabled', false);
            $('#svz-label-for-enum' + currentIDnum).show();
          }

          window.RemoveEnumRemoveTagit = function(currentIDnum){
            $('#svz-enum' + currentIDnum).hide();
            $('.tagit-choice').remove();
            $('#svz-label-for-enum' + currentIDnum).hide();
            $('#svz-schema-form-submit' + currentIDnum).remove();
          }

          $(document).on('change', '.svz-selected-type', $.debounce(TIMEOUT_DEBOUNCE, function() {
              var selectedType = $(this).val();
              var currentTabNum = $(this).attr('name').replace( /^\D+/g, '');
              var parentID = $('#svz-item-container' + $(this).attr('id').replace(/^\D+/g, '')).parent().attr('id').replace(/^\D+/g, '');
              var parentType = $('#svz-selected-type' + parentID).val();
              if (parentType){
                parentType = parentType[0];
              }

              $('.additionaloption' + currentTabNum).remove();              

              if (selectedType){
                if ((_.include(selectedType, 'number') || _.include(selectedType, 'integer')) 
                  && _.include(selectedType, 'string')
                  && parentType !== 'array') {
                  RemoveFormShowEnum(currentTabNum);

                  AppendInputFieldToForm(currentTabNum, 'Maximum length', 'svz-max-length', 'maxLength', '');
                  AppendInputFieldToForm(currentTabNum, 'Minimum length', 'svz-min-length', 'minLength', '');
                  AppendInputFieldToForm(currentTabNum, 'Minimum', 'minimum', 'minimum', 'minimum');
                  AppendCheckboxFieldToForm(currentTabNum, 'Check - num will be more than minimum', 'Exclusive minimum', 'exclusive-min-div', 'exclusiveMinimum', 'exclusiveMinimum');
                  AppendInputFieldToForm(currentTabNum, 'Maximum', 'maximum', 'maximum', 'maximum');
                  AppendCheckboxFieldToForm(currentTabNum, 'Check - num will be more than maximum', 'Exclusive maximum', 'exclusive-max-div', 'exclusiveMaximum', 'exclusiveMaximum');
                  AppendInputFieldToForm(currentTabNum, 'Default', 'svz-default', 'default', '');
                  AppendCheckboxFieldToForm(currentTabNum, 'Readonly (check for true)', '', 'svz-readonly', 'readonly', '');
                  AppendReadonlyFieldToForm(currentTabNum);
                  AppendInputFieldToForm(currentTabNum, 'Pattern (regex)', 'svz-pattern', 'pattern', '');
                  AppendSubmitBtnToForm(currentTabNum);

                } else if (_.include(selectedType, 'string') && parentType !== 'array'){
                  RemoveFormShowEnum(currentTabNum);

                  AppendInputFieldToForm(currentTabNum, 'Maximum length', 'svz-max-length', 'maxLength', '');
                  AppendInputFieldToForm(currentTabNum, 'Minimum length', 'svz-min-length', 'minLength', '');
                  AppendInputFieldToForm(currentTabNum, 'Default', 'svz-default', 'default', '');
                  AppendReadonlyFieldToForm(currentTabNum);
                  AppendInputFieldToForm(currentTabNum, 'Pattern (regex)', 'svz-pattern', 'pattern', '');
                  AppendSubmitBtnToForm(currentTabNum);

                } else if ((_.include(selectedType, 'number') || _.include(selectedType, 'integer')) && parentType !== 'array'){
                  RemoveFormShowEnum(currentTabNum);

                  AppendInputFieldToForm(currentTabNum, 'Minimum', 'minimum', 'minimum', 'minimum');
                  AppendCheckboxFieldToForm(currentTabNum, 'Check - num will be more than minimum', 'Exclusive minimum', 'exclusive-min-div', 'exclusiveMinimum', 'exclusiveMinimum');
                  AppendInputFieldToForm(currentTabNum, 'Maximum', 'maximum', 'maximum', 'maximum');
                  AppendCheckboxFieldToForm(currentTabNum, 'Check - num will be more than maximum', 'Exclusive maximum', 'exclusive-max-div', 'exclusiveMaximum', 'exclusiveMaximum');
                  AppendInputFieldToForm(currentTabNum, 'Default', 'svz-default', 'default', '');
                  AppendReadonlyFieldToForm(currentTabNum);
                  AppendSubmitBtnToForm(currentTabNum);

                } else if (_.include(selectedType, 'array') && parentType !== 'array'){
                  RemoveEnumRemoveTagit(currentTabNum);
                  AppendInputFieldToForm(currentTabNum, 'Minimum items', 'svz-min-items', 'minItems', '');
                  AppendInputFieldToForm(currentTabNum, 'Maximum items', 'svz-max-items', 'maxItems', '');
                  AppendCheckboxFieldArray(currentTabNum);
                  AppendSubmitBtnToForm(currentTabNum);
                }
              }
          }));
        
          $(document).on('change', '.minimum', function(){
            var currentID = $(this).attr('id').replace( /^\D+/g, '');
            $('#exclusive-min-div' + currentID).toggle(!!$(this).val());
          }); 
          $(document).on('change', '.maximum', function(){
            var currentID = $(this).attr('id').replace( /^\D+/g, '');
            $('#exclusive-max-div' + currentID).toggle(!!$(this).val());
          }); 

          $(document).on('change', '#svz-json-text', function(e) {
            if (e.which == 8 || e.which == 46) {
              $(this).height(parseFloat($(this).css('min-height')) != 0 ? parseFloat($(this).css('min-height')) : parseFloat($(this).css('font-size')));
            }
            while($(this).outerHeight() < this.scrollHeight + parseFloat($(this).css('borderTopWidth')) + parseFloat($(this).css('borderBottomWidth'))) {
                $(this).height($(this).height()+1);
            };

            var ajv = new Ajv({allErrors: true});
            var validate = ajv.compile(jsonPreview);
            var valid = validate(jsonPreview);
            if(!valid){
              console.log(ajv.errors);
              $('#svz-json-text-warning').show();
              $('#svz-json-text-warning').text(ajv.errors);
            } else{
              $('#svz-json-text-warning').hide();
              // $('#svz-json-text-warning').show();
              // $('#svz-json-text-warning').text('Fucking errors man! Dont know them;(( ');
            }
          });

          var jsonFromTextbox;
          var path;

          window.IteratorNestedObject = function(key, value) {
            var savepath = path;  
            path = path ? (path + "." + key) : key;

            if(path.split('.').length === 1){
              if (key === 'id'){
                $('#svz-schema-main-id').val(value);
              } else if (key === '$schema'){
                $('#svz-main-dollar-schema').val(value);
              }
              $('#svz-submit-main-options').click();
            } else if(path.split('.').length === 3){
              $('#svz-add-item1').click();
              var currentItemID = $('#svz-container1').children().eq(-2).attr('id').replace( /^\D+/g, '');
              $('form#svz-schema-form' + currentItemID + ' :input[name="' + 'key' + String(currentItemID) + '"]').val(path.split('.')[2]);
              $('form#svz-schema-form' + currentItemID + ' :input').each(function(){
                if ($(this).attr('name')){
                  $.each(Object.byString(jsonFromTextbox, path), function(key, value){
                    if ($('form#svz-schema-form' + currentItemID + ' :input[name="' + String(key) + String(currentItemID) + '"]').val()){
                    } else{
                      $('form#svz-schema-form' + currentItemID + ' :input[name="' + String(key) + String(currentItemID) + '"]').val(value);
                    }
                    
                    if ($('form#svz-schema-form' + currentItemID + ' :input[name="' + String(key) + String(currentItemID) + '"]').attr('name') === 'type' + String(currentItemID)){
                      $('form#svz-schema-form' + currentItemID + ' :input[name="' + String(key) + String(currentItemID) + '"]').multiselect('refresh');
                    }                    
                  });
                }
              });
              $('#svz-schema-form-submit' + currentItemID).click();
            } else if(path.split('.').length % 2 !== 0){
              try{
                var containerLabelID = $('#svz-container1').find('label:contains("' + path.split('.').reverse()[2] + '")').attr('id');
                if (containerLabelID){
                  if (containerLabelID.replace(/[0-9]/g, '') === 'svz-label-container'){
                    var itemLabelID = $('#svz-container' + containerLabelID.replace( /^\D+/g, '')).find('label:contains("New schema")').attr('id');
                    var currentItemID = itemLabelID.replace( /^\D+/g, '');
                  }
                }

                var assignedEnum = $('#svz-enum' + currentItemID).tagit('assignedTags');
                $('form#svz-schema-form' + currentItemID + ' :input[name="' + 'key' + String(currentItemID) + '"]').val(path.split('.').reverse()[0]);
                $('form#svz-schema-form' + currentItemID + ' :input[name="' + 'enum' + String(currentItemID) + '"]').val(path.split('.').reverse()[0]);

                // $('#svz-enum' + currentID).tagit('assignedTags').val(path.split('.').reverse()[0]);


                $('form#svz-schema-form' + currentItemID + ' :input').each(function(){
                  if ($(this).attr('name')){
                    $.each(Object.byString(jsonFromTextbox, path), function(key, value){
                      if ($('form#svz-schema-form' + currentItemID + ' :input[name="' + String(key) + String(currentItemID) + '"]').val()){
                      } else{
                        $('form#svz-schema-form' + currentItemID + ' :input[name="' + String(key) + String(currentItemID) + '"]').val(value);
                      }
                      
                      if ($('form#svz-schema-form' + currentItemID + ' :input[name="' + String(key) + String(currentItemID) + '"]').attr('name') === 'type' + String(currentItemID)){
                        $('form#svz-schema-form' + currentItemID + ' :input[name="' + String(key) + String(currentItemID) + '"]').multiselect('refresh');
                      }                    
                    });
                  }
                });
                $('#svz-schema-form-submit' + currentItemID).click();
              } catch(e){}
            } else if ((path.split('.').length % 2 === 0) && (_.include(path, 'items'))){
              var containerLabelID = $('#svz-container1').find('label:contains("' + path.split('.').reverse()[1] + '")').attr('id');

              if (containerLabelID){
                if (containerLabelID.replace(/[0-9]/g, '') === 'svz-label-container'){
                  var itemLabelID = $('#svz-container' + containerLabelID.replace( /^\D+/g, '')).find('label:contains("New schema")').attr('id');
                  var currentItemID = itemLabelID.replace( /^\D+/g, '');
                }
              }
              var assignedEnum = $('#svz-enum' + currentItemID).tagit('assignedTags');
              $('form#svz-schema-form' + currentItemID + ' :input[name="' + 'key' + String(currentItemID) + '"]').val(path.split('.').reverse()[0]);
              $('form#svz-schema-form' + currentItemID + ' :input[name="' + 'enum' + String(currentItemID) + '"]').val(path.split('.').reverse()[0]);

              // $('#svz-enum' + currentID).tagit('assignedTags').val(path.split('.').reverse()[0]);

              $('form#svz-schema-form' + currentItemID + ' :input').each(function(){
                if ($(this).attr('name')){
                  $.each(Object.byString(jsonFromTextbox, path), function(key, value){
                    if ($('form#svz-schema-form' + currentItemID + ' :input[name="' + String(key) + String(currentItemID) + '"]').val()){
                    } else{
                      $('form#svz-schema-form' + currentItemID + ' :input[name="' + String(key) + String(currentItemID) + '"]').val(value);
                    }
                    
                    if ($('form#svz-schema-form' + currentItemID + ' :input[name="' + String(key) + String(currentItemID) + '"]').attr('name') === 'type' + String(currentItemID)){
                      $('form#svz-schema-form' + currentItemID + ' :input[name="' + String(key) + String(currentItemID) + '"]').multiselect('refresh');
                    }                    
                  });
                }
              });
              $('#svz-schema-form-submit' + currentItemID).click();

            }

            if (typeof value === "object") {
                $.each(value, IteratorNestedObject);
            }  
            path = savepath;
          }

          $(document).on('click', '#svz-generate-inputs', function(){
            $('#svz-container1').html('<button id="svz-add-item1" class="btn btn-secondary svz-add-item" type="button">+</button>');
            allKeys = [];
            try{              
              jsonFromTextbox = JSON.parse(editor.getValue());
              $.each(jsonFromTextbox, IteratorNestedObject);
            } catch(e){
              console.log(e);
            }
          });

          var required = [];
          var properties = {};
          var formProperties = {};
          var formFields = [];

          window.ShowJSONPreview = function(){
            if(_.isEmpty(jsonPreview['schema'])){
              jsonPreview['schema'] = {};
            }
            jsonPreview['schema']['type'] = 'object';
            jsonPreview['schema']['properties'] = properties;
            
            if (_.isEmpty(jsonPreview['form'])){
              jsonPreview['form'] = {};
            }
            jsonPreview['form']['fields'] = formFields;

            if (required != ''){
              jsonPreview['required'] = required;
            } else{
              delete jsonPreview['required'];
            }

            $('#svz-json-text-header').hide();
            editor.setValue(JSON.stringify(jsonPreview, undefined, 2));
            // $('#svz-json-text').height($('#svz-json-text').prop('scrollHeight'));


            // var ajv = new Ajv({allErrors: true});
            // var validate = ajv.compile(jsonPreview);
            // var valid = validate(jsonPreview);
            // if(!valid){
            //   console.log(ajv.errors);
            // } else{
            //   console.log('VALIDDD');
            // }
            
          }


          Object.byString = function(o, s) {
            if (!s || !o) return;
            s = s.replace(/\[(\w+)\]/g, '.$1'); // convert indexes to properties
            s = s.replace(/^\./, '');           // strip a leading dot
            var a = s.split('.');
            for (var i = 0, n = a.length; i < n; ++i) {
              var k = a[i];
              if (k in o) {
                  o = o[k];
              } else {
                  return;
              }
            }
            return o;
          }

          window.search = function(path, obj, target) {
            for (var k in obj) {
              if (obj.hasOwnProperty(k)){
                if (obj[k] === target){
                  return path + "['" + k + "']";
                }
                else if (typeof obj[k] === "object") {
                    var result = search(path + "['" + k + "']", obj[k], target);
                    if (result){
                      return result;
                    }
                }
              }      
            }
            return false;
          }

          window.HandleMainOptionsFormSubmit = function(){
            $.each($('#svz-main-form-schema-options').serializeArray(), function(i, field) {
              if (field.value === 'on'){
                field.value = 'true';
              }
              if (_.include($('form#svz-main-form-schema-options :input[name="' + field.name + '"]').attr('class'), 'svz-form-main-options')){
                if (_.isEmpty(jsonPreview['form'])){
                  jsonPreview['form'] = {};
                }

                jsonPreview['form'][field.name] = field.value;
              } else{
                if(field.value){
                  if (_.isEmpty(jsonPreview['schema'])){
                    jsonPreview['schema'] = {};
                  }
                  jsonPreview['schema'][field.name] = field.value;
                }
              }
              
            });

            $('#svz-main-options').slideUp();
            $('#svz-toggle-main-options').show();
          }

          $(document).on('click', '#svz-toggle-main-options', function(){
            $('#svz-main-options').slideToggle();
          }); 
                        
          window.HandleFormFormSubmit = function(currentObject, currentID){
            var currentFormProperties = {}

            if ($('#svz-label-item' + $(currentObject).attr('id').replace( /^\D+/g, '')).html()){
              var currentKey = $('#svz-label-item' + $(currentObject).attr('id').replace( /^\D+/g, '')).html();
            } else{
              var currentKey = $('#svz-label-container' + $(currentObject).attr('id').replace( /^\D+/g, '')).html();
            }

            var currentID = currentID.replace( /^\D+/g, ''); 
            var schemaFormDataArray = $('#svz-for-form-form' + currentID).serializeArray();
            schemaFormDataArray = schemaFormDataArray.filter(function(n){return n.value !== ''});

            currentFormProperties['key'] = currentKey;
            jQuery.each( schemaFormDataArray, function( i, field ) {
              if (field.value === 'on'){
                field.value = 'true';
              }
              currentFormProperties[field.name.replace(/[0-9]/g, '')] = field.value;
            });

            formFields.push(currentFormProperties);
          }

          var typeArrayKeysPaths = {};
          
          window.HandleSchemaFormSubmit = function(currentObject, currentID){
            var currentID = currentID.replace( /^\D+/g, '');
            if($('#svz-key-warning').is(':visible')){
              return false;
            }

            if (_.include(allKeys, $('#svz-key' + currentID).val()) 
                && $('#svz-key' + currentID).val() != $('#svz-label-item' + currentID).html() 
                  && $('#svz-key' + currentID).val() != $('#svz-label-container' + currentID).html()){
              $('#svz-key-warning' + currentID).show();
              $('#svz-key' + currentID).css('border-color', '#ff0000');
              return false;
            } else{
              $('#svz-key-warning' + currentID).hide();
              $('#svz-key' + currentID).css('border-color', '#cccccc');
            }
            var currentKey = $('#svz-label-item' + currentID).html();
            if (!currentKey){
              currentKey = $('#svz-label-container' + currentID).html();
            }

            if (allKeys && _.include(allKeys, currentKey)){ 
              var pathToValue = '';
              var currentKeyItem = $('#svz-label-item' + $(currentObject).attr('id').replace( /^\D+/g, '')).html();
              if(! currentKeyItem){
                currentKeyItem = $('#svz-label-container' + $(currentObject).attr('id').replace( /^\D+/g, '')).html();
              }
              var currentKeyContainer = $('#svz-label-container' + $(currentObject).parents(':eq(6)').attr('id').replace( /^\D+/g, '')).html();
              var allPaths = GetAllPaths(properties);
              var chosenKey = $('#svz-key' + currentID).val();

              for (var i = 0; i < allPaths.length; i++){
                if (_.include(allPaths[i], currentKeyItem)){
                  pathToValue = allPaths[i].split('.' + currentKeyItem + '.type')[0];
                  break;
                } else if (_.include(allPaths[i], currentKeyContainer + '.')){
                  var pathIsReady = true;
                  pathToValue = allPaths[i].split('.type')[0];
                  if (pathToValue.split('.').length != 1){
                    pathToValue += '.properties';
                  }
                }
              }
              if (!pathIsReady){
                pathToValue = pathToValue.split(currentKey)[0]
                if (pathToValue && pathToValue.slice(-1) != '.'){
                  pathToValue += '.' + currentKey;
                } else{
                  pathToValue += currentKey;
                }

                if(!pathToValue){
                  pathToValue = typeArrayKeysPaths[currentKeyContainer];
                }
              }
             
              if (pathToValue.split('.').slice(-1)[0] != 'type'){
                pathToValue = pathToValue.split('.type')[0];
              }

              try{
                var thisProperties = Object.byString(properties, pathToValue);
              } catch(e){}
              
              if (pathToValue.split('.').length == 1){
                thisProperties = properties;
              }

              if (pathToValue.split('.').slice(-1)[0] != 'properties' && pathToValue.split('.').slice(-1)[0] != 'items' && pathToValue.split('.').length != 1){
                pathToValue = pathToValue.split(pathToValue.split('.').slice(-1)[0])[0];
              }
                            
              var typesFromSelect = $('#svz-selected-type' + currentID).val();
              var typesFromSelectArray = $.map(typesFromSelect, function(value, index) {
                  return [value];
              });

              var schemaFormDataArray = $('#svz-schema-form' + currentID).serializeArray();
              var toDeleteRequired = true;

              if (_.isEmpty(thisProperties[currentKey])){
                thisProperties[currentKey] = {};
              }

              if (typesFromSelectArray.length === 1){
                thisProperties[currentKey]['type'] = typesFromSelectArray[0];
              } else{
                thisProperties[currentKey]['type'] = typesFromSelectArray;
              }
              
              schemaFormDataArray = schemaFormDataArray.filter(function(n){return n.value !== ''});

              jQuery.each( schemaFormDataArray, function( i, field ) {
                if (field.value === 'on'){
                  field.value = 'true';
                }

                if(field.name === 'key' + currentID){
                  chosenKey = field.value;
                  allKeys.push(chosenKey);
                } else if(field.name === 'required' + currentID){
                  toDeleteRequired = false;
                  if (field.value && !(_.include(required, chosenKey))) {
                    if (_.include(required, $('#svz-label-item' + currentID).html())){
                      required.splice(_.indexOf(required, $('#svz-label-item' + currentID).html()), 1);
                    }
                    required.push(chosenKey);
                  } 
                } else{
                  if (field.name.replace(/[0-9]/g, '') != 'tags' 
                      && field.name.replace(/[0-9]/g, '') != 'type'
                        && field.name.replace(/[0-9]/g, '') != 'key'){
                    thisProperties[currentKey][field.name.replace(/[0-9]/g, '')] = field.value;
                  }
                }
              });
              if (chosenKey){
                $('#svz-label-item' + currentID).html(chosenKey);
                $('#svz-label-container' + currentID).html(chosenKey);
              }else{
                $('#svz-label-item' + currentID).html('SVZlabel' + currentID);
                $('#svz-label-container' + currentID).html('SVZlabel' + currentID);
              }
              
              var assignedEnum = $('#svz-enum' + currentID).tagit('assignedTags');
              if (assignedEnum != '') {
                thisProperties[currentKey]['enum'] = assignedEnum;
              }
              
              if (toDeleteRequired){
                required.splice(_.indexOf(required, chosenKey), 1);
              }

              if (chosenKey != currentKey){
                try{
                  Object.defineProperty(Object.byString(properties, pathToValue), chosenKey, Object.getOwnPropertyDescriptor(Object.byString(properties, pathToValue), currentKey));
                  delete Object.byString(properties, pathToValue)[currentKey];
                } catch(e){
                  Object.defineProperty(properties, chosenKey, Object.getOwnPropertyDescriptor(properties, currentKey));
                  delete properties[currentKey];
                }
              }
              allKeys.splice(_.indexOf(allKeys, currentKey), 1);
              return;
            }

            var typesFromSelect = $('#svz-selected-type' + currentID).val();
            var typesFromSelectArray = $.map(typesFromSelect, function(value, index) {
                return [value];
            });
            
            var chosenKey = '';
            var schemaFormDataArray = $('#svz-schema-form' + currentID).serializeArray();
            var currentProperties = {};
            var toDeleteRequired = true;

            if (typesFromSelectArray.length === 1){
              currentProperties['type'] = typesFromSelectArray[0];
            } else{
              currentProperties['type'] = typesFromSelectArray;
            }
            
            schemaFormDataArray = schemaFormDataArray.filter(function(n){return n.value !== ''});

            jQuery.each( schemaFormDataArray, function( i, field ) {
              if (field.value === 'on'){
                field.value = 'true';
              }
              if(field.name === 'key' + currentID){
                chosenKey = field.value;
                allKeys.push(chosenKey);
              } else if(field.name === 'required' + currentID){
                toDeleteRequired = false;
                if (field.value && !(_.include(required, chosenKey))) {
                    if (_.include(required, $('#svz-label-item' + currentID).html())){
                      required.splice(_.indexOf(required, $('#svz-label-item' + currentID).html()), 1);
                    }
                    required.push(chosenKey);
                } 
              } else{
                if (field.name.replace(/[0-9]/g, '') != 'tags' && field.name.replace(/[0-9]/g, '') != 'type'){
                  currentProperties[field.name.replace(/[0-9]/g, '')] = field.value;
                }
              }
            });

            if (chosenKey){
              $('#svz-label-item' + currentID).html(chosenKey);
              $('#svz-label-container' + currentID).html(chosenKey);
            }else{
              $('#svz-label-item' + currentID).html('SVZlabel' + currentID);
              $('#svz-label-container' + currentID).html('SVZlabel' + currentID);
            }

            var assignedEnum = $('#svz-enum' + currentID).tagit('assignedTags');
            if (assignedEnum != '') {
              currentProperties['enum'] = assignedEnum;
            }
            
            if (toDeleteRequired){
              required.splice(_.indexOf(required, chosenKey), 1);
            }

            if (!$(currentObject).parents(':eq(11)').html()){
              properties[chosenKey] = currentProperties;
            } else{
              var pathToValue = '';
              var currentKeyItem = $('#svz-label-item' + $(currentObject).attr('id').replace( /^\D+/g, '')).html();
              var currentKeyContainer = $('#svz-label-container' + $(currentObject).parents(':eq(6)').attr('id').replace( /^\D+/g, '')).html();
              var allPaths = GetAllPaths(properties);

              for (var i = 0; i < allPaths.length; i++){
                if (_.include(allPaths[i], currentKeyItem)){
                  pathToValue = allPaths[i].split('.' + currentKeyItem + '.type')[0];
                  break;
                } else if (_.include(allPaths[i], currentKeyContainer + '.')){
                  pathToValue = allPaths[i].split('.type')[0];
                }
              }
              
              if(!pathToValue){
                pathToValue = typeArrayKeysPaths[currentKeyContainer];
              }

              var parentType = String($('#svz-selected-type' + $(currentObject).parents(':eq(6)').attr('id').replace( /^\D+/g, '')).val());
              if (parentType !== 'object' && parentType !== 'array'){
                if(_.isEmpty(Object.byString(properties, pathToValue)['properties'][chosenKey])){
                  Object.byString(properties, pathToValue)['items'] = currentProperties;
                }else{
                  Object.byString(properties, pathToValue)['properties'][chosenKey] = currentProperties;
                }
              } else if (parentType === 'object'){
                if(_.isEmpty(Object.byString(properties, pathToValue)['properties'])){
                  Object.byString(properties, pathToValue)['properties'] = {};
                }
                Object.byString(properties, pathToValue)['properties'][chosenKey] = currentProperties;
              } else if (parentType === 'array'){
                if (_.isEmpty(Object.byString(properties, pathToValue)['items'])){
                  Object.byString(properties, pathToValue)['items'] = {};
                }
                Object.byString(properties, pathToValue)['items'] = currentProperties;
              }
            }

            try {
              var sortableItemsArray = $('.container').sortable('toArray');
              var sortableItemsArrayLength = sortableItemsArray.length;
              for (var i = 0; i < sortableItemsArrayLength; i++) {
                if (_.include(allKeys, $('#' + sortableItemsArray[i]).find('.svz-label-item').html())){
                  properties[$('#' + sortableItemsArray[i]).find('.svz-label-item').html()]['ordering'] = i + 1;
                }
              }
            } catch(err) {}

            if(_.include(typesFromSelectArray, 'object')){
              AppendObjectArrayForm(currentID, 'object');
            } else if (_.include(typesFromSelectArray, 'array')){
              AppendObjectArrayForm(currentID, 'array');
            }

            $('#svz-form-li' + currentID).css('display', 'inline-block');
            
            if (_.include(typesFromSelectArray, 'array') || _.include(typesFromSelectArray, 'object')){
              var parentID = $(currentObject).parents(':eq(7)').attr('id');
              var currentItemLabel = $('#svz-label-container' + currentID).html();
              
              if(parentID === 'svz-container1'){
                typeArrayKeysPaths[currentItemLabel] = chosenKey;
              } else{
                var parentLabel = $('#' + parentID).find('label').html();
                var allPaths = GetAllPaths(properties);

                for (var i = 0; i < allPaths.length; i++){
                  if (_.include(allPaths[i], parentLabel)){
                    var pathToParent = allPaths[i].split('.type')[0];
                    typeArrayKeysPaths[currentItemLabel] = pathToParent + '.items';
                    break;
                  }
                }
                if (!pathToParent){
                  typeArrayKeysPaths[currentItemLabel] = typeArrayKeysPaths[parentLabel] + '.items';
                }
              }
            }
          } 
        });
      })(jQuery);