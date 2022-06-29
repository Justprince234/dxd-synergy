function toggle(source) {
    checkboxes = document.getElementsByName('foo');
    for (var checkbox in checkboxes)
      checkbox.checked = source.checked;
  }

  function toggle(source) {
    checkboxes = document.getElementsByName('foo');
    for (var i = 0, n = checkboxes.length; i < n; i++) {
      checkboxes[i].checked = source.checked;
    }
  }