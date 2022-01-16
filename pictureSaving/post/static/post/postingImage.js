// Get the cover
var cover = document.getElementById("box-cover");

// Get the <span> element that closes the cover
var span = document.getElementsByClassName("close-icon")[0];

// When the user clicks on <span> (x), close the cover
span.onclick = function() {
    cover.style.display = "none";
}
// When the user clicks anywhere outside of the cover, close it
window.onclick = function(event) {
    if (event.target == cover) {
    cover.style.display = "none";
    }
}

// when clickk on button add post will pop up dialog
$('#open-dialog').click(function(){
    console.log('clicking to create new post')
    cover.style.display ="block"
});

// click button post image then trigger input file
$('#btn-post').click(function(){ 
    $('#btn-post').hide();
    $('#imgupload').trigger('click');
});

// click to back
$('.previous-dialog').click(function(){
    $('#btn-confirm').hide();
    $('.previous-dialog').hide();
    $('.container-second').hide()
    $('.container-dot-dialog').empty();
    $('.container-slideshow-dialog').empty() // making slide show empty
    $('#icon').show()
    $('#btn-post').show();
    $('.container-title').text('Create a new Strawberry')
})

// show to review image
function show()
{
    $('.container-dot-dialog').empty();
    $('.container-slideshow-dialog').empty() // making slide show empty
    $('.container-title').text('Review a new Strawberry')
    $('#icon').hide()
    $('.previous-dialog').show();
    $('.container-second').show()

    var len = event.target.files.length // get length of file will posting
    if(len > 0){
        html ='';
        var index = 1;
        //making images to review
        for (file of event.target.files)
        {
            var src = URL.createObjectURL(file);
            html+= addingImageHtml(src,index,len)
            index++;
        }
        // making arrow
        if(len>1){
            html+='<a class="prev-dialog">'+iconNext+';</a>'
            html+='<a class="next-dialog">'+iconPrevious+';</a>'
            html+='<br>'
        }
        // making dot pullet
        html_dot=''
        if(len>1){
            for (var i=0; i< event.target.files.length;i++){
                html_dot+='<span class="dot-dialog" onclick="handleImageDialog.currentSlide('+ (i+1).toString()+')"></span>'
            }
        }
        // console.log(html)
        // console.log(html_dot)

        // append to class container-slideshow-dialog
        $('.container-slideshow-dialog').append(html)
        // append to class container-dot-container
        $('.container-dot-dialog').append(html_dot)
        // making first image block
        var slideIndex = 1;
        handleImageDialog.showSlides(slideIndex);
        // contro image show
        $('.prev-dialog').click(function(){
            handleImageDialog.plusSlides(-1);
        })
        $('.next-dialog').click(function(){
            handleImageDialog.plusSlides(1);   
        })
        $('#btn-confirm').show();
        
    }
}

// function helper to generating image in myslide div
function addingImageHtml(src,index,len){
    html =''
    html+='<div class="mySlides-dialog fade">'
    html+='<div class="numbertext-dialog ">'+index.toString()+'/'+len.toString()+'</div>'
    html+='<img src="'+src+'" style="width:100%">'
    html+='</div>'
    return html
}


// function helper to get csrf in cookies to pass to header
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


// confirm adding new data to db using formData obj to post to Django server
$('#btn-confirm').click(postDataToDB);
// POST using axious
function postDataToDB(){
    console.log("on click")
    var fd = new FormData();
    var caption = document.getElementById('NewPostCaption').value
    console.log(caption)
    fd.append('caption', caption);
    var description =  document.getElementById('NewPostDescription').value
    console.log(description)
    fd.append('description', description);
    var fileList = document.getElementById('imgupload').files;
    for (file of fileList){
        fd.append('fileList', file);
    }
    console.log(fileList)
    // console.log(fileArray)
    console.log(getCookie('csrftoken'))
    axios({
        method: 'post',
        url: '/post',
        headers: {
            'X-CSRFTOKEN': getCookie('csrftoken'),
            'Content-Type': "multipart/form-data"
         },
        data: fd
      });
    cover.style.display = "none";
}

