<script>
  import Sidebar from './lib/Sidebar.svelte';
  import Block from './lib/Block.svelte';
  import Floor from './lib/Floor.svelte';

  const canvasWidth = 600;
  const canvasHeight = 600;
  let floorColour = $state('#dfaa38');
  let floorBoardWidth = $state(10);
  let selected = $state(null);

  let svg;
  let dragging = false;
  let displayItems = $state([]);

  function getSvgPoint(event) {
    const pt = svg.createSVGPoint();
    pt.x = event.clientX;
    pt.y = event.clientY;
    return pt.matrixTransform(svg.getScreenCTM().inverse());
  }

  function selectItem(event, item) {
    event.stopPropagation();
    dragging = true;
    const pt = getSvgPoint(event);
    selected = { item, offsetX: pt.x - item.x, offsetY: pt.y - item.y };
  }

  function drag(event) {
    if (!dragging) return;

    const pt = getSvgPoint(event);
    selected.item.x = Math.round(10 * (pt.x - selected.offsetY)) / 10;
    selected.item.y = Math.round(10 * (pt.y - selected.offsetY)) / 10;

    displayItems = displayItems;
  }

  function endDrag() {
    dragging = false;
  }

</script>

<div class=container>
  <Sidebar bind:displayItems bind:floorColour bind:floorBoardWidth bind:selected />

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
      {#each displayItems as item (item.id)}
        <g
          transform={`translate(${item.x - item.width / 2},${item.y - item.height / 2})`}
          onpointerdown={(e) => selectItem(e, item)}
          style="cursor:grab"
        >
          <image href={item.href} width={item.width} height={item.height} />
        </g>
      {/each}
    </svg>
  </main>
</div>

<style>

</style>
