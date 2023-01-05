// Submit post on submit
$('#post-form').on('submit', function(event){
    event.preventDefault();
    console.log("Form submitted!")  // sanity check
    create_post();
});

//function create_post() {
//    console.log("create post is working!") // sanity check
//    console.log($('#post-message'))
//    console.log($('#post'))
//    console.log($('#post-text').val())
////    console.log($('post').val())
//};

function create_post() {
    console.log("create post is working!") // sanity check
    $.ajax({
        url : "index", // the endpoint
        type : "POST", // http method
        data : {
            name : $('#post-name').val(),
            email: $('#post-email').val(),
            subject: $('#post-subject').val(),
            message: $('#post-message').val()}, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $('#post-name').val(''); // remove the value from the input
            $('#post-email').val(''); // remove the value from the input
            $('#post-subject').val(''); // remove the value from the input
            $('#post-message').val(''); // remove the value from the input
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};