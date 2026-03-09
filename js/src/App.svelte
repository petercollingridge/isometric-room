<script>
  import Block from './lib/Block.svelte';

  const canvasWidth = 600;
  const canvasHeight = 600;
  let floorColour = $state('#dd8822');
</script>

<div class=container>
  <div class="sidebar">
    <label>
      Floor:
      <input type="color" bind:value={floorColour}>
    </label>
  </div>
  <main>
    <svg class="canvas" width={`${canvasWidth}px`} height={`${canvasHeight}px`}>
      <Block x={canvasWidth / 2 - 9} y={20} width1={300} width2={10} height={300} fill="#eeeebb"/>
      <Block x={canvasWidth / 2 + 9} y={20} width1={10} width2={300} height={300} fill="#ffffdd"/>
      <Block x={canvasWidth / 2} y={300 + 17} width1={300} width2={300} height={8} fill={floorColour}/>
    </svg>
  </main>
</div>

<style>

</style>
