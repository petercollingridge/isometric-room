<script>
  import Block from './Block.svelte';
  import { darkenHex, DX, DY } from '../utils';

  const {x, y, width1, width2, height, fill, floorBoardWidth} = $props();

  const dx = $derived(DX);
  const dy = $derived(DY);

  const positions = $derived.by(() => {
    const nBoards = 48 - floorBoardWidth;
    const boardWidth = width1 / nBoards;
    const plank = [];
    for (let i = 1; i < nBoards; i++) {
      plank.push([x - dx * i * boardWidth, y - 4 + dy * i * boardWidth]);
    }
    return plank;
  });

</script>

<g>
  <Block x={x} y={y} width1={width1} width2={width2} height={15} fill="#d8d8d8"/>
  <Block x={x} y={y - 4} width1={width1} width2={width2} height={height} fill={fill}/>
  {#each positions as [px, py]}
    <path d={`M${px},${py}l${dx * width2},${dy * width2}v${height}`} stroke={darkenHex(fill, 0.2)} stroke-width="1" fill="none"/>
  {/each}
</g>
