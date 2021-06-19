```javascript
var slider = document.createEvent('MouseEvents');
slider.initEvent('mousedown', true, false);
//定位滑块的标签
document.querySelector(".geetest_slider_button").dispatchEvent(slider);
slider = document.createEvent('MouseEvents');
slider.initEvent('mousemove', true, true);
Object.defineProperty(slider, 'clientX', {
 get() {
  // 滑行距离
  return 360;
 }
});
//滑块元素
document.querySelector("#nc_2_n1z").dispatchEvent(slider);
```

