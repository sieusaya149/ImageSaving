// define path to icon image path
const pathIcon = 'static/post/img/'

const iconLike = pathIcon+'like.PNG'
const iconComment = pathIcon +'comment.PNG'
const iconSend = pathIcon +'send.PNG'
const iconSave = pathIcon +'save.PNG'
const iconSmile = pathIcon +'smile.PNG'
const iconOption = pathIcon + 'option.PNG'

// icon profile maybe change depend on user
var iconProfile= pathIcon+'cover 1.png'

// define symbol
const iconNext = '&#10094'
const iconPrevious = '&#10095'


// define url
const domain ='//127.0.0.1:8000/'
const apiGetPostInfo = domain+'api/getPostInfo/' // need /postId/
const apiGetImageInfo = domain+'api/getImageInfo/' // need /postId/
const apiGetLike = domain+'api/getHeartInfo/' // need /postId/
const apiGetComment = domain+'api/getCommentInfo/' // need /postId/



// Object Get PostData
class PostData{
    constructor(high, low, allow){ 
        console.log('INNITIAL POST OBJ')
        this.lastestPost=high
        this.oldestPost=low
        this.allowGet = allow
    }
}
PostData.prototype.getPost = function (){
    console.log('getting post now')
    let html =''
    // if can get more post in DB
    var self = this;
    if(self.allowGet == true){
        $.ajax({
            async: false,
            type: 'get',
            url: apiGetPostInfo + self.lastestPost.toString() +'/',
            dataType:'json',
            success: function(posts){
                // if see post data in DB change lastestPost and oldestPost
                if(posts.length !=0){
                    self.oldestPost = getLastPostId(posts)
                    self.lastestPost = self.oldestPost;
                    console.log("value upper Post now " +  self.lastestPost.toString())
                    console.log("value last Post now " + self.oldestPost.toString())
                    prepareObj = new Prepare()
                    html+=prepareObj.preparePost(posts) // render by Render object
                }
                else{
                    console.log("No data");
                    self.allowGet=false
                }
            }
        });
    }
    else{
        console.log("No data in DB");
        self.allowGet=false
    }
    return html
}

// Object Get ImageData
class ImageData{
    constructor(postId){
       this.ofPost = postId
    }
}

ImageData.prototype.getImages= function (){
    console.log("get image for post id: "+ this.ofPost)
    let html =''
    var self = this;
        $.ajax({
            async: false,
            type: 'get',
            url: apiGetImageInfo+ self.ofPost +'/',
            dataType:'json',
            success: function(images){
                // if has any image render it
                if(images.length !=0){
                    console.log('this post now is '+ self.ofPost)
                    html = prepareObj.prepareImage(images,self.ofPost)
                    console.log(html)
                }
                else{
                    console.log("No images")
                }
            }
        });
    return html
}

class InteractData{
    constructor(postId){
        this.ofPost = postId
    }
}
InteractData.prototype.getLikes = function (){
    var numberLikes;
    $.ajax({
        async: false,
        type: 'get',
        url: apiGetComment+this.ofPost+'/',
        dataType:'json',
        success: function(listLike){
            numberLikes = listLike.length;
        }
    });
    return numberLikes;
}
InteractData.prototype.getComments = function (){
    var self = this
    html =''
        $.ajax({
            async: false,
            type: 'get',
            url: apiGetComment+self.ofPost+'/',
            dataType:'json',
            success: function(listComment){
                $.each(listComment, function(index,comment){
                    html+='<p class="description"><span>'+comment.userId+ '</span> '+comment.content+'</p>'
                })
            }
        });
    return html;
}


class Prepare{

}
Prepare.prototype.preparePost = function(posts){
    let html = ''
    $.each(posts, function(index,post){
        // loop through post then call ajax get image
        html+='<div class="post post'+post.postId+'">'
        html+='<div class="info">'
        html+='<div class="user">'
        html+='<div class="profile-pic"><img src="'+ iconProfile +'" alt=""></div>'
        html+='<p class="username">#'+post.caption+'</p>'
        html+='</div>'
        html+='<img src="'+ iconOption +'" class="options" alt="">'
        html+='</div>'
        // create object get Image
        console.log('post id now is'+post.postId)
        imageData = new ImageData(post.postId)
        html+=imageData.getImages()
        // end get image
        html+='    '
        html+='<div class="postContent">'
        html+='<div class="reaction-wrapper">'
        html+='<img src="'+ iconLike +'" class="icon" alt="">'
        html+='<img src="'+ iconComment +'" class="icon" alt="">'
        html+='<img src="'+ iconSend +'" class="icon" alt="">'
        html+='<img src="'+ iconSave +'" class="save icon" alt="">'
        html+='</div>'
        interactData = new InteractData(post.postId)
        numberLikes = interactData.getLikes()
        html+='<p class="likes">'+numberLikes.toString() +' likes</p>'
        html+= interactData.getComments()
        html+='<p class="post-time">2 minutes ago</p>'
        html+='</div>'
        html+='<div class="comment-wrapper">'
        html+='<img src="'+ iconSmile +'" class="icon" alt="">'
        html+='<input type="text" class="comment-box" placeholder="Add a comment">'
        html+='<button class="comment-btn">post</button>'
        html+='</div>'
        html+='</div>'
    })
    return html;
}
Prepare.prototype.prepareImage = function(images,postId){
    let html=''
    console.log(postId)
    html+='<div id="slideShow' +postId+'" class="slideshow-container">'
    $.each(images, function(index,image){
        // loop through post then call ajax get image
        html+='<div  class="mySlides' +postId+' fade">'
        html+='<img src="'+image.path+'" style="width:100%">'
        html+='</div>'
    })
    if(images.length>1){
        html+='<a class="prev" onclick="plusSlides(-1,'+postId+')">'+iconNext+';</a>'
        html+='<a class="next" onclick="plusSlides(1,'+postId+')">'+iconPrevious+';</a>'
    }
    html+='</div>'
    html+='<br>'
    if(images.length>1){
        html+='<div style="text-align:center">'
        for(var i = 0; i < images.length;i++){
            html+=' <span  class="dot" class="dot'+postId+'" onclick="currentSlide('+(i+1).toString()+','+postId+')"></span> '
        }
        html+='</div>'
    }
    html+='<script>'
    html+='var slideIndex = 1;'
    html+='showSlides(slideIndex,'+postId+');'
    html+='</script>'

    return html
}
function getLastPostId(posts){
    return posts.at(-1).postId.toString();
}

class Render{

}
Render.prototype.renderHtml= function (html){
    $('.left-col').append(html)
}
post = new PostData(high=1000,low=0,allow = true)
render = new Render()
window.onscroll = function() {
    if (window.innerHeight + window.pageYOffset >= document.body.offsetHeight) {
        console.log("loadmoredata")
        console.log("post moi nhat"+post.lastestPost.toString())
        console.log("post cu nhat"+post.oldestPost.toString())
        render.renderHtml(post.getPost())
    }
 }