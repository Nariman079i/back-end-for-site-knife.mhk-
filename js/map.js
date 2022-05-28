;(function() {
  if (typeof ymaps === 'undefined') {
    return;
  }

  ymaps.ready(function () {
    var myMap = new ymaps.Map('ymap', {
            center: [42.982104, 47.467141],
            zoom: 16
        }, {
            searchControlProvider: 'yandex#search'
        }),

        myPlacemark = new ymaps.Placemark(myMap.getCenter(), {
            balloonContent: 'г. Махачкала, Гайдара Гаджиева, пр-т. Акушинского,13'
        }, {
            iconLayout: 'default#image',
            iconImageHref: '',
            iconImageSize: [40, 63.2],
            iconImageOffset: [-50, -38]
        });

    myMap.geoObjects.add(myPlacemark);

    myMap.behaviors.disable('scrollZoom');
});


})();