<script>
  import Block from './lib/Block.svelte';
  import Floor from './lib/Floor.svelte';

  const canvasWidth = 600;
  const canvasHeight = 600;
  let floorColour = $state('#dfaa38');
  let floorBoardWidth = $state(10);
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
    <svg class="canvas" width={`${canvasWidth}px`} height={`${canvasHeight}px`}>
      <Block x={canvasWidth / 2 - 9} y={20} width1={300} width2={10} height={300} fill="#eeeebb"/>
      <Block x={canvasWidth / 2 + 9} y={20} width1={10} width2={300} height={300} fill="#ffffdd"/>
      <Floor x={canvasWidth / 2} y={300 + 15} width1={300} width2={300} height={5} fill={floorColour} floorBoardWidth={floorBoardWidth}/>
    </svg>
  </main>
</div>

<style>

</style>
