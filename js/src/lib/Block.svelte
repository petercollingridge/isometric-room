<script>
  import { darkenHex } from '../utils';

  const {x, y, width1, width2, height, fill} = $props();

  const THETA = Math.atan(Math.sin(Math.PI / 6))
  const DX = Math.cos(THETA)
  const DY = Math.sin(THETA)

  const getTop = () => {
    const dx1 = DX * width1;
    const dy1 = DY * width1;
    const dx2 = DX * width2;
    const dy2 = DY * width2;
    return `M${x},${y}l${-dx1},${dy1} ${dx2},${dy2} ${dx1},${-dy1}z`;
  }

  const getLeftSide = () => {
    const x1 = x + DX * width2;
    const y1 = y + DY * width2;
    const dx = DX * width1;
    const dy = DY * width1;
    return `M${x1},${y1}v${height}l${-dx},${dy}v${-height}z`;
  }

  const getRightSide = () => {
    const x1 = x - DX * width1;
    const y1 = y + DY * width1;
    const dx = DX * width2;
    const dy = DY * width2;
    return `M${x1},${y1}v${height}l${dx},${dy}v${-height}z`;
  }

  const getStroke = () => {
    return darkenHex(fill, 0.1);
  }

</script>

<g>
  <path d={getTop()} fill={fill} stroke={getStroke()}/>
  <path d={getLeftSide()} fill={fill} stroke={getStroke()}/>
  <path d={getRightSide()} fill={fill} stroke={getStroke()}/>
</g>
