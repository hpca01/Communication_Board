tinymce.init({
  selector: 'textarea',
  branding: false,
  height: 300,
  menubar: false,
  plugins: [
    'advlist autolink lists charmap print preview textcolor',
    'searchreplace visualblocks code fullscreen',
    'insertdatetime contextmenu paste code help wordcount'
  ],
  toolbar: 'insert | undo redo |  formatselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | removeformat | help',
  content_css: [
    '//fonts.googleapis.com/css?family=Lato:300,300i,400,400i',
    '//www.tinymce.com/css/codepen.min.css']
});