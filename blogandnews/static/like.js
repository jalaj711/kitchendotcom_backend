// console.log("like comment share")

let liked = localStorage.getItem('liked')
if(liked)
    liked = JSON.parse(liked)
else
    liked = new Object()

const likeLink =  document.getElementById("like-link")
const blogId = likeLink.getAttribute("blogId")
const likeTargetLink = likeLink.getAttribute('href')


likeLink.addEventListener('click', (e)=>{
    e.preventDefault()
    if(liked[blogId]){
        alert('liked already')
        return 
    }
    liked[blogId] = 'liked'
    localStorage.setItem( 'liked', JSON.stringify(liked) )
    console.log('redirecting')
    window.location.href = likeTargetLink    
})
