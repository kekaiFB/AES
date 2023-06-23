$(document).ready(function(){

    var flag = true
    let timerId = setInterval(() => flag=true, 500);

    $('.element').on( "click", function() {
        $('.element').removeClass('text-warning') 
        $('.element').addClass('text-dark')  
        $(this).addClass('text-warning')
        $(this).removeClass('text-dark')

        if (flag){
            var img = $('div .'+$(this).attr('id')+'_image').html()
            var content = $('div .'+$(this).attr('id')+'_content').html()
        
            //массив с моделями
            var mp4_arr = []
            var fbx_arr = $('div .'+$(this).attr('id')+'_fbx')
            .map(function (index, item) {
            var val = item.innerHTML.replaceAll(' ', '').replaceAll('\n', '')
            if (val.slice(-3) == 'fbx')
            {
                return val
            }
            else 
            if (val.slice(-3) == 'mp4')
            {
                mp4_arr.push(val)
            }
            })
            .get();
        
            $('div .content_div').html('')
            $('div .content_div').append(content)
    
            for ( var i = 0; i < mp4_arr.length; i ++ ) {           
                $('div .content_div').append("<video class='rounded mt-2' width='600' src="+ mp4_arr[i]+"  controls></video>")
            }
            

            $('a').on( "click", function() {
              var arr = $(this).attr('class').substring(5).split(' ')
              $(arr[0]).click()
              $(arr[1]).click()
              });
        
        

            $('div .content_div').append('<br>')
            $('div .content_div').append(img)
            render_my_fbx(fbx_arr[0], 'div .fbx_div')   

            flag = false
        }
  });

  
  $('.tab').on( "click", function() {
    $('.tab').removeClass('text-warning') 

    $('.element').hide()
    $('.'+$(this).attr('class').split(' ').slice(-1)[0]).show()   
 
    $(this).addClass('text-warning')
});
  
  
  
  
  
  
  
  
  function render_my_fbx(filename_fbx, path_finish_div) {
  
      var materialShader;
      var clock = new THREE.Clock();
      var mixers = [];
  
      scene = new THREE.Scene();
      scene.background = new THREE.Color( 0xffffff );
      scene.fog = new THREE.Fog( scene.background, 200, 1000 );
  
      var camera = new THREE.PerspectiveCamera(45, 1, 1, 1000);
      camera.position.set( 100, 200, 300 );
  
      renderer = new THREE.WebGLRenderer( { antialias: true } );
      renderer.setPixelRatio( window.devicePixelRatio );
      renderer.shadowMap.enabled = true;
  
      // тут
      var canvas = renderer.domElement
      $(path_finish_div).html(canvas);
      // var canvas = renderer.domElement
      // canvas.width =$(path_finish_div)[0].offsetWidth
      // canvas.height = $(path_finish_div)[0].offsetHeight
      // $(path_finish_div).html(canvas);
  
  
      controls = new THREE.OrbitControls( camera, renderer.domElement );
      controls.target.set( 0, 100, 0 );
      controls.update();
  
      light = new THREE.HemisphereLight( 0xffffff, 0x444444 );
      light.position.set( 0, 200, 0 );
      scene.add( light );
  
      light = new THREE.DirectionalLight( 0xffffff );
      light.position.set( 0, 200, 100 );
      light.castShadow = true;
      light.shadow.camera.top = 180;
      light.shadow.camera.bottom = - 100;
      light.shadow.camera.left = - 120;
      light.shadow.camera.right = 120;
      scene.add( light );
  
      // ground
      var mesh = new THREE.Mesh( new THREE.PlaneBufferGeometry( 2000, 2000 ), new THREE.MeshPhongMaterial( { color: 0x004080, depthWrite: false } ) );
      mesh.rotation.x = - Math.PI / 2;
      mesh.receiveShadow = true;
      scene.add( mesh );
  
      var grid = new THREE.GridHelper( 2000, 20, 0x00ffff, 0x00ffff );
      grid.material.opacity = 0.2;
      grid.material.transparent = true;
      scene.add( grid );
  
      // model
      var loader = new THREE.FBXLoader();
      loader.load(filename_fbx, function ( object ) {
  
      object.mixer = new THREE.AnimationMixer( object );
      mixers.push( object.mixer );
  
      var action = object.mixer.clipAction( object.animations[ 0 ] );
      action.play();
  
      object.traverse( function ( child ) {
  
          if ( child.isMesh ) {
  
          child.castShadow = true;
          child.receiveShadow = true;
  
          }
  
      } );
  
      var box = new THREE.Box3().setFromObject(object);
      var size = new THREE.Vector3();
      box.getSize(size);
      object.children[2].material = new THREE.MeshBasicMaterial({color: 0xffddff, skinning: true});
      object.children[1].material.color.set(0xff00ff);
      object.children[1].material.onBeforeCompile = function ( shader ) {
          shader.uniforms.time = { value: 0 };
          shader.uniforms.size = { value: size};
          shader.uniforms.color1 = {value: new THREE.Color(0xff0080)};
          shader.uniforms.color2 = {value: new THREE.Color(0xfff000)};
          shader.vertexShader = 'varying vec4 vWorldPosition;\n' + shader.vertexShader;
          shader.vertexShader = shader.vertexShader.replace(
          '#include <worldpos_vertex>',
          [
              '#include <worldpos_vertex>',
              'vWorldPosition = modelMatrix * vec4( transformed, 1.0 );'
          ].join( '\n' )
          );
          shader.fragmentShader = 'uniform float time;\nuniform vec3 size;\nuniform vec3 color1;\nuniform vec3 color2;\nvarying vec4 vWorldPosition;\n' + shader.fragmentShader;
          shader.fragmentShader = shader.fragmentShader.replace(
          '#include <dithering_fragment>',
          [
              '#include <dithering_fragment>',
              'float gridRatio = sin( time ) * 0.1875 + 0.3125;', // 0.125 .. 0.5
              'vec3 m = abs( sin( vWorldPosition.xyz * gridRatio ) );',
              'vec3 gridColor = mix(color1, color2, vWorldPosition.y / size.y);',
              'gl_FragColor = vec4( mix( gridColor, gl_FragColor.rgb, m.x * m.y * m.z ), diffuseColor.a );'
          ].join( '\n' )
          );
          materialShader = shader;
      };
      scene.add( object );
      // console.log( object );
  
      } );
  
      render();
  
      function render() {
      if (resize(renderer)) {
          camera.aspect = canvas.clientWidth / canvas.clientHeight;
          camera.updateProjectionMatrix();
      }
      
      if ( mixers.length > 0 ) {
          for ( var i = 0; i < mixers.length; i ++ ) {
          mixers[ i ].update( clock.getDelta() );
          }
      }
  
      if (materialShader) materialShader.uniforms.time.value = performance.now() / 1000;
      
      renderer.render(scene, camera);
      requestAnimationFrame(render);
      }
  
      function resize(renderer) {
      const canvas = renderer.domElement;
      const width = canvas.clientWidth;
      const height = canvas.clientHeight;
      const needResize = canvas.width !== width || canvas.height !== height;
      if (needResize) {
          renderer.setSize(width, height, false);
      }
      return needResize;
      }
  }
  });
  