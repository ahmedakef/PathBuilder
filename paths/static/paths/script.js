document.addEventListener("DOMContentLoaded", function(){
    // Handler when the DOM is fully loaded
    var slug = new Slugit()
    
    slug.doSlug({
        event: 'keydown',
        timeout: 200,
        el: '#id_name',
        target: '#id_slug',
    })
  });
  
