document.addEventListener('DOMContentLoaded',()=>{
  const menu=document.querySelector('.menu-btn'); const nav=document.querySelector('.nav-links');
  if(menu&&nav){menu.addEventListener('click',()=>{const open=nav.classList.toggle('open');menu.setAttribute('aria-expanded',String(open));});}
  document.querySelectorAll('[data-copy]').forEach(btn=>btn.addEventListener('click',async()=>{
    const text=btn.getAttribute('data-copy')||''; const before=btn.textContent;
    try{await navigator.clipboard.writeText(text);}catch(e){const t=document.createElement('textarea');t.value=text;document.body.appendChild(t);t.select();document.execCommand('copy');t.remove();}
    btn.textContent=btn.dataset.copied||'Copied'; setTimeout(()=>btn.textContent=before,1800);
  }));
});