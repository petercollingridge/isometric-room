<script>
  import Block from './lib/Block.svelte';
  import Floor from './lib/Floor.svelte';

  const canvasWidth = 600;
  const canvasHeight = 600;
  let floorColour = $state('#dfaa38');
  let floorBoardWidth = $state(10);

  let svg;
  let dragging = null;

  let items = $state([
    { id: 1, x: 100, y: 100, href: "/src/assets/picture_frame.svg" },
    { id: 2, x: 200, y: 150, href: "/src/assets/picture_frame.svg" }
  ]);

  function getSvgPoint(event) {
    const pt = svg.createSVGPoint();
    pt.x = event.clientX;
    pt.y = event.clientY;
    return pt.matrixTransform(svg.getScreenCTM().inverse());
  }

  function startDrag(event, item) {
    event.stopPropagation();
    const pt = getSvgPoint(event);
    dragging = { item, offsetX: pt.x - item.x, offsetY: pt.y - item.y };
  }

  function drag(event) {
    if (!dragging) return;

    const pt = getSvgPoint(event);
    dragging.item.x = pt.x - dragging.offsetY;
    dragging.item.y = pt.y - dragging.offsetY;

    items = items;
  }

  function endDrag() {
    dragging = null;
  }

</script>

<div class=container>
  <div class="sidebar">
  <div>
    <label>
      Floor:
      <input type="color" bind:value={floorColour}>
    </label>
    </div>
    <div>
    <label>
      Floorboard width:
      <input type="range" bind:value={floorBoardWidth} min={8} max={40}>
    </label>
    </div>
  </div>

  <main>
    <!-- svelte-ignore a11y_no_static_element_interactions -->
    <svg
      class="canvas"
      bind:this={svg}
      width={`${canvasWidth}px`}
      height={`${canvasHeight}px`}
      onpointermove={drag}
      onpointerup={endDrag}  
    >
      <Block x={canvasWidth / 2 - 9} y={20} width1={300} width2={10} height={300} fill="#eeeebb"/>
      <Block x={canvasWidth / 2 + 9} y={20} width1={10} width2={300} height={300} fill="#ffffdd"/>
      <Floor x={canvasWidth / 2} y={300 + 10} width1={300} width2={300} height={5} fill={floorColour} floorBoardWidth={floorBoardWidth}/>

      <!-- Draggable objects -->
      {#each items as item (item.id)}
        <g
          transform={`translate(${item.x},${item.y})`}
          onpointerdown={(e) => startDrag(e, item)}
          style="cursor:grab"
        >
          <image href={item.href} width="50" height="50" />
        </g>
      {/each}
    </svg>
  </main>
</div>

<style>

</style>
