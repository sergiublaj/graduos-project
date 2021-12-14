$('#form_profile_edit_button').on('click', () => {
    $('#inputUsername').prop('readonly', false);
    $('#inputEmail').prop('readonly', false);
    $('#inputPhone').prop('readonly', false);
    $('#inputCountry').prop('readonly', false);
    $('#inputAddress').prop('readonly', false);
    
    $('#form_profile_edit_button').remove();
 
    let changePicture = '<input type="file" class="form-control" id="inputPhoto" name="inputPhoto">';
    $('#profile-photo-div').append(changePicture);

    let saveButton = '<button id="form_profile_save_button" class="btn btn-primary"> <i class="fas fa-save"></i> Save </button>';
    let cancelButton = '<button id="form_profile_cancel_button" class="btn btn-danger"> <i class="fas fa-minus-circle"></i> Cancel </button>';
 
    let formButtonsArea = $('.form-buttons-area');
    formButtonsArea.append(saveButton);
    formButtonsArea.append(cancelButton);
 });
 
 
 $('#form_profile_save_button').on('click', () => {
     $('#form_profile').submit();
    
    revertButtons();
 });

 $('#form_profile_cancel_button').on('click', () => {
   $('#form_profile').submit((e) => e.preventDefault());

    revertButtons();
 });

 function revertButtons() {
    $('#form_profile :input').prop('readonly', true);
 
    $('#form_profile_save_button').remove();
    $('#form_profile_cancel_button').remove();
 
    let editButton = '<button id="form_profile_edit_button" class="btn btn-primary"> <i class="fas fa-edit"></i> Edit profile </button>';
 
    $('.form-buttons-area').append(editButton);
 }