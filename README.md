balanced-code-challenge
=======================

Code challenge addressing this gist: https://gist.github.com/mjallday/fddde8cdac01cf7ced72


1. Testing - did some of this
2. What I would change:
    * The API call isn't really an API call. It currently renders to a template so that I can see the images in the browser.
    * I would do a better job of checking the inputs that I'm given since I currently just drop them straight into the database.
    * Better abstractions for the code so its easier to test. Also figure out better organization for my code files.
    * The entire environment for this project is a mini application, so it really depends on what you might expect from production. Is there going to be a huge server load? Do you need to store a lot of photos? 
3.  If I were adding PUT, DELETE, and PATCH I'd first make this an actual API call that returns json or xml. Flask is nice because you can specify which types of methods a function accept. You'd want the image ID for each of these calls to edit, replace, or delete the image.
4.  Currently I'm storing an image SRC and not actually loading the image and saving it, so my system doesn't really care how big the image is. If I were to have users upload an image or load the file from the given SRC, I would probably put a file size limit first and foremost (I think there are default file size limits already). Haven't really done a lot with large image file uploads, so I'd probably go do a bunch of research.
5.  I'm not sure exactly what type of post processing is being done, but you can set up asynchronous tasks to do longer jobs post-processing the images depending on how quickly users will want post-processed images. Also something I haven't done a lot of, so I don't know all the considerations. 
