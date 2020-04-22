let isPostsOnlyActive = false;
let isBlogsOnlyActive = false;
function postsOnly(){
    if(isPostsOnlyActive && isBlogsOnlyActive){
        let element = document.getElementById("posts-only");
        element.style.color = "#ffffff";
        element.style.backgroundColor = "#2b2b2b";
        let posts=document.getElementsByClassName("posts");
        for(let i=0; i<posts.length; i+=1){
            posts[i].style.display="none";
        }
        isPostsOnlyActive = false;
    }
    else if (isPostsOnlyActive && !isBlogsOnlyActive){
    let element = document.getElementById("posts-only");
    element.style.color = "#ffffff";
    element.style.backgroundColor = "#2b2b2b";
    let blogs=document.getElementsByClassName("blogs");
    for(let i=0; i<blogs.length; i+=1){
        blogs[i].style.display="block";
    }
    let posts=document.getElementsByClassName("posts");
    for(let i=0; i<blogs.length; i+=1){
        posts[i].style.display = "block";
    }
    isPostsOnlyActive = false;
    }else if (!isPostsOnlyActive && !isBlogsOnlyActive){
        let element = document.getElementById("posts-only");
        element.style.color = "#1a1a1a";
        element.style.backgroundColor = "#ff7357";
        let blogs=document.getElementsByClassName("blogs");
        for(let i=0; i<blogs.length; i+=1){
            blogs[i].style.display="none";
        }
        isPostsOnlyActive = true;
    }
    else{
        let element = document.getElementById("posts-only");
        element.style.color = "#1a1a1a";
        element.style.backgroundColor = "#ff7357";
        let posts = document.getElementsByClassName("posts");
        for(let i=0; i<posts.length; i+=1){
            posts[i].style.display="block";
        }
        isPostsOnlyActive = true;
    }
}
function blogsOnly(){
    if (isBlogsOnlyActive && isPostsOnlyActive){
    let element = document.getElementById("blogs-only");
    element.style.color = "#ffffff";
    element.style.backgroundColor = "#2b2b2b";
    let posts=document.getElementsByClassName("posts");
    for(let i=0; i<posts.length; i+=1){
        posts[i].style.display="block";
    }
    let blogs=document.getElementsByClassName("blogs");
    for(let i=0; i<blogs.length; i+=1){
        blogs[i].style.display="none";
    }
    isBlogsOnlyActive = false;
    }else if (isBlogsOnlyActive && !isPostsOnlyActive){
        let element = document.getElementById("blogs-only");
        element.style.color = "#ffffff";
        element.style.backgroundColor = "#2b2b2b";
        let posts=document.getElementsByClassName("posts");
        for(let i=0; i<posts.length; i+=1){
            posts[i].style.display="block";
        }
        let blogs=document.getElementsByClassName("blogs");
        for(let i=0; i<blogs.length; i+=1){
            blogs[i].style.display="block";
        }
        isBlogsOnlyActive = false;
    }else if(!isBlogsOnlyActive && isPostsOnlyActive){
        blogs = document.getElementsByClassName("blogs");
        for(let i=0; i<blogs.length; i+=1){
            blogs[i].style.display="block";
        }
        posts = document.getElementsByClassName("posts");
        for(let i=0; i<posts.length; i+=1){
            posts[i].style.display="block";
        }
        let element = document.getElementById("blogs-only");
        element.style.color = "#1a1a1a";
        element.style.backgroundColor = "#ff7357";
        isBlogsOnlyActive = true;
    }
    else{
        let element = document.getElementById("blogs-only");
        element.style.color = "#1a1a1a";
        element.style.backgroundColor = "#ff7357";
        blogs = document.getElementsByClassName("blogs");
        for(let i=0; i<blogs.length; i+=1){
            blogs[i].style.display="block";
        }
        posts = document.getElementsByClassName("posts");
        for(let i=0; i<posts.length; i+=1){
            posts[i].style.display="none";
        }
        isBlogsOnlyActive = true;
    }
}