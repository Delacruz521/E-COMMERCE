// Set current year in footer
document.getElementById('year').textContent = new Date().getFullYear();

const mobileToggle = document.getElementById('mobileToggle');
const mobileMenu = document.getElementById('mobile-menu');
const mobileClose = document.getElementById('mobileClose');

mobileToggle.addEventListener('click', ()=>{
  const open = mobileMenu.style.display === 'block';
  mobileMenu.style.display = open ? 'none' : 'block';
  mobileToggle.setAttribute('aria-expanded', String(!open));
});
mobileClose.addEventListener('click', ()=>{
  mobileMenu.style.display='none';
  mobileToggle.setAttribute('aria-expanded','false')
});
function closeMobile(){
  mobileMenu.style.display='none';
  mobileToggle.setAttribute('aria-expanded','false')
}

// Fake contact form handler
function handleContact(e){
  e.preventDefault();
  const name = document.getElementById('name').value.trim();
  const email = document.getElementById('email').value.trim();
  const msg = document.getElementById('message').value.trim();
  if(!name || !email || !msg){
    alert('Please fill the required fields');
    return;
  }
  alert('Thanks '+name+' — your message is queued (demo).');
  e.target.reset();
}

// Fade-in animations when elements enter viewport
const revealEls = document.querySelectorAll('.fade-in');
const io = new IntersectionObserver(entries=>{
  entries.forEach(ent=>{
    if(ent.isIntersecting){
      ent.target.classList.add('visible');
      ent.target.style.opacity = 1;
    }
  });
},{threshold:0.08});
revealEls.forEach(el=>io.observe(el));
