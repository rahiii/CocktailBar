// sidebar js functionality

function openSidebar() {
    const overlay = document.getElementById('sidebarOverlay');
    const sidebar = document.getElementById('quizSidebar');
    overlay.style.display = 'block';
    sidebar.classList.add('active');
    document.body.classList.add('no-scroll');
  }
  
  function closeSidebar() {
    const overlay = document.getElementById('sidebarOverlay');
    const sidebar = document.getElementById('quizSidebar');
    sidebar.classList.remove('active');
    setTimeout(() => overlay.style.display = 'none', 300);
    document.body.classList.remove('no-scroll');
  }