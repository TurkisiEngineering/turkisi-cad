#!/bin/bash
# P01 Guard - SolidCraft komut dizisi uretici. Cikti: build.json (stdout)
# Kullanim: bash gen.sh [asama] > build.json   (asama: 1=dis govde, 2=+flans/boss, 3=tam)
STAGE=${1:-9}
# --- ayni degerler, secim noktalari icin (mm) ---
S=0.069756; C=0.997564; NX=0.721392; NY=0.692527; CY=-0.09375; W=0.125
f(){ awk "BEGIN{printf \"%.6f\", ($1)*25.4}"; }
pt(){ echo "[$(f "$1"),$(f "$2"),$(f "$3")]"; }
SEP=""
cmd(){ printf '%s{"command":"%s","params":%s}\n' "$SEP" "$1" "$2"; SEP=","; }
par(){ local U=""; [ "$3" = u ] && U=",\"unit\":\"\""; [ -n "$3" ] && [ "$3" != u ] && U=",\"unit\":\"$3\""; cmd parameters.add "{\"name\":\"$1\",\"expression\":\"$2\"$U,\"comment\":\"$4\"}"; }

# Kapali bir cadir/tumsek govdesi kuran fonksiyon. $1=onek(o|i) $2=govde adi $3=duvar ofseti ifadesi (0 veya wall) $4=alt y ifadesi
tent_hump(){
  local P=$1 B=$2 OF=$3 YB=$4
  local RC="(R_crown-$OF)" RA="(R_arch-$OF)" DE="(d_end-$OF)" DS="(d_slope-$OF)" DSi="(d_side-$OF)" DH="(d_hend-$OF)" DL="(d_leg-$OF)"
  local XE="(($DE - sin(draft)*$YB)/cos(draft))"
  local DET="(cos(draft)*n_sy - sin(draft)*n_sx)"
  local CX="(($DE*n_sy - sin(draft)*$DS)/$DET)" CYY="((cos(draft)*$DS - n_sx*$DE)/$DET)"
  local TX="(n_sx*$RC)" TY="(cy + n_sy*$RC)"
  # --- 3.1 cadir profili (XY)
  cmd sketch.create "{\"plane\":\"XY\",\"name\":\"${P}_tent_profile\"}"
  cmd sketch.line "{\"points\":[[\"-$XE\",\"$YB\"],[\"$XE\",\"$YB\"],[\"$CX\",\"$CYY\"],[\"$TX\",\"$TY\"]]}"
  cmd sketch.arc.three_point "{\"start\":[\"$TX\",\"$TY\"],\"end\":[\"-$TX\",\"$TY\"],\"through\":[\"0\",\"cy+$RC\"]}"
  cmd sketch.line "{\"points\":[[\"-$TX\",\"$TY\"],[\"-$CX\",\"$CYY\"],[\"-$XE\",\"$YB\"]]}"
  cmd sketch.finish "{}"
  cmd solid.extrude "{\"distance\":\"4\",\"direction\":\"symmetric\",\"operation\":\"new\",\"body_name\":\"$B\",\"name\":\"${P}_tent_extrude\"}"
  # yan duvar dilimi (YZ: sketch x=+Y, y=+Z)
  local ZL="((($DSi) - sin(draft)*(y_bot-0.5))/cos(draft))" ZH="((($DSi) - sin(draft)*2.5)/cos(draft))"
  cmd sketch.create "{\"plane\":\"YZ\",\"name\":\"${P}_tent_sidewalls\"}"
  cmd sketch.line "{\"points\":[[\"y_bot-0.5\",\"-$ZL\"],[\"y_bot-0.5\",\"$ZL\"],[\"2.5\",\"$ZH\"],[\"2.5\",\"-$ZH\"]],\"closed\":true}"
  cmd sketch.finish "{}"
  cmd solid.extrude "{\"distance\":\"10\",\"direction\":\"symmetric\",\"operation\":\"intersect\",\"targets\":[\"$B\"],\"name\":\"${P}_tent_trim\"}"
  # --- 3.3/1 yan duvar kenar yuvarlatmasi
  local w=0; [ "$P" = i ] && w=$W
  local de=$(awk "BEGIN{print 2.902310-$w}") ds=$(awk "BEGIN{print 0.860129-$w}") rc=$(awk "BEGIN{print 1.9375-$w}") dsl=$(awk "BEGIN{print 1.872576-$w}")
  local E sz
  for sz in 1 -1; do E="";
    for sx in 1 -1; do
      E="$E$(pt "$sx*($de+$S)/$C" "-1" "$sz*($ds+$S)/$C"),"
      E="$E$(pt "$sx*($dsl-$NY*0.5)/$NX" "0.5" "$sz*($ds-$S*0.5)/$C"),"
    done
    cmd solid.fillet "{\"edges\":[${E%,}],\"radius\":\"$5\",\"body\":\"$B\",\"name\":\"${P}_tent_side_round_z$sz\"}"
  done
  # --- 3.2 tumsek (XY)
  local XL="(($DL - sin(draft)*$YB)/cos(draft))" AX="(cos(draft)*$RA)" AY="(cy + sin(draft)*$RA)"
  cmd sketch.create "{\"plane\":\"XY\",\"name\":\"${P}_hump_profile\"}"
  cmd sketch.line "{\"points\":[[\"-$XL\",\"$YB\"],[\"$XL\",\"$YB\"],[\"$AX\",\"$AY\"]]}"
  cmd sketch.arc.three_point "{\"start\":[\"$AX\",\"$AY\"],\"end\":[\"-$AX\",\"$AY\"],\"through\":[\"0\",\"cy+$RA\"]}"
  cmd sketch.line "{\"points\":[[\"-$AX\",\"$AY\"],[\"-$XL\",\"$YB\"]]}"
  cmd sketch.finish "{}"
  cmd solid.extrude "{\"distance\":\"5\",\"direction\":\"symmetric\",\"operation\":\"new\",\"body_name\":\"${B}_hump\",\"name\":\"${P}_hump_extrude\"}"
  local HL="((($DH) - sin(draft)*(y_bot-0.5))/cos(draft))" HH="((($DH) - sin(draft)*2)/cos(draft))"
  cmd sketch.create "{\"plane\":\"YZ\",\"name\":\"${P}_hump_endfaces\"}"
  cmd sketch.line "{\"points\":[[\"y_bot-0.5\",\"-$HL\"],[\"y_bot-0.5\",\"$HL\"],[\"2\",\"$HH\"],[\"2\",\"-$HH\"]],\"closed\":true}"
  cmd sketch.finish "{}"
  cmd solid.extrude "{\"distance\":\"10\",\"direction\":\"symmetric\",\"operation\":\"intersect\",\"targets\":[\"${B}_hump\"],\"name\":\"${P}_hump_trim\"}"
  local dl=$(awk "BEGIN{print 1.305960-$w}") dh=$(awk "BEGIN{print 1.608303-$w}") ra=$(awk "BEGIN{print 1.3125-$w}")
  for sz in 1 -1; do E="";
    for sx in 1 -1; do E="$E$(pt "$sx*($dl+$S)/$C" "-1" "$sz*($dh+$S)/$C"),"; done
    E="$E$(pt 0 "$CY+$ra" "$sz*($dh-$S*($CY+$ra))/$C"),"
    cmd solid.fillet "{\"edges\":[${E%,}],\"radius\":\"$6\",\"body\":\"${B}_hump\",\"name\":\"${P}_hump_end_round_z$sz\"}"
  done
  cmd solid.combine "{\"target\":\"$B\",\"tools\":[\"${B}_hump\"],\"operation\":\"join\",\"name\":\"${P}_unite_hump\"}"
  # --- 3.3/3 tumsek-cadir icbukey yuvarlatma
  for sz in 1 -1; do E="";
    for sx in 1 -1; do E="$E$(pt "$sx*($dl+$S)/$C" "-1" "$sz*($ds+$S)/$C"),"; done
    E="$E$(pt 0 "$CY+$ra" "$sz*($ds-$S*($CY+$ra))/$C"),"
    cmd solid.fillet "{\"edges\":[${E%,}],\"radius\":\"$7\",\"body\":\"$B\",\"name\":\"${P}_hump_tent_concave_z$sz\"}"
  done
}

echo '{"commands":['
cmd document.units '{"units":"in"}'
par wall 0.125 "" "et kalinligi"
par draft "4 deg" deg "tum duvarlarin kalip acisi"
par y_bot -1.53125 "" "flans alti (montaj yuzu) y"
par fl_t 0.125 "" "flans kalinligi"
par cy -0.09375 "" "tepe/kemer silindir ekseni y (x=0)"
par R_crown 1.9375 "" "dis tepe yayi yaricapi"
par R_arch 1.3125 "" "dis tumsek kemer yaricapi"
par n_sx 0.721392 u "egim duzlemi normali x bileseni"
par n_sy 0.692527 u "egim duzlemi normali y bileseni"
par d_end 2.902310 "" "dis uc duvar duzlemi sabiti"
par d_side 0.860129 "" "dis yan duvar duzlemi sabiti"
par d_hend 1.608303 "" "dis tumsek uc yuzu duzlemi sabiti"
par d_slope "n_sy*cy + R_crown" "" "dis egim duzlemi sabiti (tepe yayina teget)"
par d_leg "sin(draft)*cy + R_arch" "" "dis tumsek bacak duzlemi sabiti (kemere teget)"
par R_side 0.375 "" "cadir yan kenar disbukey yuvarlatma (ic: R_side-wall)"
par R_hump 0.375 "" "tumsek uc yuzu disbukey yuvarlatma (ic: R_hump-wall)"
par R_conc 0.125 "" "tumsek-cadir icbukey yuvarlatma (ic: R_conc+wall)"
par y_cav "y_bot - 0.12" "" "bosluk govdesinin alt uzatmasi"
tent_hump o "P01 Guard" 0 y_bot R_side R_hump R_conc
[ $STAGE -ge 2 ] && tent_hump i "Cavity" wall y_cav "R_side-wall" "R_hump-wall" "R_conc+wall"
if [ $STAGE -ge 3 ]; then
par boss_d 0.8125 "" "boss capi"
par boss_h 0.0875 "" "boss ust yuzunun dis yuzeyden yuksekligi (eksen uzerinde)"
par boss_r 0.1 "" "boss tabani icbukey yuvarlatma"
par rec_d 0.5625 "" "boss ici girinti capi"
par R_open 0.1 "" "alt agiz kenari disbukey yuvarlatma"
par Px 1.369085 "" "egim bossu ekseninin dis egim duzlemini kestigi nokta x"
par Py "(d_slope - n_sx*Px)/n_sy" "" "egim bossu nokta y (dis egim duzleminde)"
# --- 3.6 flans (XZ duzlemi, sketch x=+X, y=-Z; y_bot ofsetli)
cmd sketch.create '{"plane":"XZ","offset":"y_bot","name":"flange_outline"}'
F=$(awk 'BEGIN{
 n=split("3.891473,-0.594612 L 3.891473,0.594612 A2.641780,0.594612,1.249693 2.641780,1.844305 L 1.995220,1.844305 A1.042140,1.613720,0.980580 1.043100,2.594305 L -1.043100,2.594305 A-1.042140,1.613720,0.980580 -1.995220,1.844305 L -2.641780,1.844305 A-2.641780,0.594612,1.249693 -3.891473,0.594612 L -3.891473,-0.594612 A-2.641780,-0.594612,1.249693 -2.641780,-1.844305 L -2.186970,-1.844305 A-1.041530,-1.344612,1.249693 -1.041530,-2.594305 L 1.041530,-2.594305 A1.041530,-1.344612,1.249693 2.186970,-1.844305 L 2.641780,-1.844305 A2.641780,-0.594612,1.249693 3.891473,-0.594612",t," ");
 split(t[1],p,","); x0=p[1]; z0=p[2]; out=""; sep="";
 for(i=2;i<=n;i+=2){ split(t[i+1],q,","); x1=q[1]; z1=q[2];
   if(t[i]=="L"){ out=out sep sprintf("{\"command\":\"sketch.line\",\"params\":{\"points\":[[\"%.6f\",\"%.6f\"],[\"%.6f\",\"%.6f\"]]}}",x0,-z0,x1,-z1) }
   else { split(substr(t[i],2),c,","); cx=c[1]; cz=c[2]; r=c[3]; ux=(x0-cx)+(x1-cx); uz=(z0-cz)+(z1-cz); l=sqrt(ux*ux+uz*uz);
     mx=cx+r*ux/l; mz=cz+r*uz/l;
     out=out sep sprintf("{\"command\":\"sketch.arc.three_point\",\"params\":{\"start\":[\"%.6f\",\"%.6f\"],\"end\":[\"%.6f\",\"%.6f\"],\"through\":[\"%.6f\",\"%.6f\"]}}",x0,-z0,x1,-z1,mx,-mz) }
   sep=","; x0=x1; z0=z1 }
 print out }')
printf ',%s\n' "$F"
cmd sketch.finish '{}'
cmd solid.extrude '{"distance":"fl_t","operation":"join","targets":["P01 Guard"],"name":"flange_extrude"}'
# --- 3.4 bosslar: uzun silindir + R0.1 taban yuvarlatma + ust duzlemde kirpma
cmd solid.cylinder '{"diameter":"boss_d","height":"0.6","base":["0","cy+R_crown-0.35","0"],"axis":"Y","operation":"join","targets":["P01 Guard"],"name":"boss_top"}'
cmd solid.cylinder '{"diameter":"boss_d","height":"0.6","base":["Px-0.3*n_sx","Py-0.3*n_sy","0"],"axis":[0.721392,0.692527,0],"operation":"join","targets":["P01 Guard"],"name":"boss_slope_px"}'
cmd solid.cylinder '{"diameter":"boss_d","height":"0.6","base":["-(Px-0.3*n_sx)","Py-0.3*n_sy","0"],"axis":[-0.721392,0.692527,0],"operation":"join","targets":["P01 Guard"],"name":"boss_slope_nx"}'
[ -n "$BOSS_ROUND" ] && { YT=$(awk 'BEGIN{print sqrt(1.9375^2-0.40625^2)-0.09375}')
cmd solid.fillet "{\"edges\":[$(pt 0.40625 $YT 0),$(pt -0.40625 $YT 0)],\"radius\":\"boss_r\",\"body\":\"P01 Guard\",\"name\":\"boss_top_base_round\"}"
}
[ -n "$BOSS_ROUND" ] && for sx in 1 -1; do
  E="$(pt "$sx*(1.369085+0.40625*$NY)" "1.277826-0.40625*$NX" 0)"
  cmd solid.fillet "{\"edges\":[$E],\"radius\":\"boss_r\",\"body\":\"P01 Guard\",\"name\":\"boss_slope_base_round_x$sx\"}"
done
cmd solid.cylinder '{"diameter":"1.4","height":"0.5","base":["0","cy+R_crown+boss_h","0"],"axis":"Y","operation":"cut","targets":["P01 Guard"],"name":"boss_top_trim"}'
cmd solid.cylinder '{"diameter":"1.2","height":"0.5","base":["Px+boss_h*n_sx","Py+boss_h*n_sy","0"],"axis":[0.721392,0.692527,0],"operation":"cut","targets":["P01 Guard"],"name":"boss_slope_trim_px"}'
cmd solid.cylinder '{"diameter":"1.2","height":"0.5","base":["-(Px+boss_h*n_sx)","Py+boss_h*n_sy","0"],"axis":[-0.721392,0.692527,0],"operation":"cut","targets":["P01 Guard"],"name":"boss_slope_trim_nx"}'
# --- 3.5 ic bosluk kesimi + girintiler
cmd solid.combine '{"target":"P01 Guard","tools":["Cavity"],"operation":"cut","name":"cavity_cut"}'
cmd solid.cylinder '{"diameter":"rec_d","height":"0.3+boss_h","base":["0","cy+R_crown-wall-0.3","0"],"axis":"Y","operation":"cut","targets":["P01 Guard"],"name":"recess_top"}'
cmd solid.cylinder '{"diameter":"rec_d","height":"0.3+boss_h","base":["Px-(wall+0.3)*n_sx","Py-(wall+0.3)*n_sy","0"],"axis":[0.721392,0.692527,0],"operation":"cut","targets":["P01 Guard"],"name":"recess_slope_px"}'
cmd solid.cylinder '{"diameter":"rec_d","height":"0.3+boss_h","base":["-(Px-(wall+0.3)*n_sx)","Py-(wall+0.3)*n_sy","0"],"axis":[-0.721392,0.692527,0],"operation":"cut","targets":["P01 Guard"],"name":"recess_slope_nx"}'
fi
if [ $STAGE -ge 4 ]; then
  XB=$(awk 'BEGIN{print (2.777310+0.069756*1.53125)/0.997564}')
  cmd solid.fillet "{\"edges\":[$(pt $XB -1.53125 0),$(pt -$XB -1.53125 0)],\"radius\":\"R_open\",\"body\":\"P01 Guard\",\"name\":\"opening_round\"}"
fi
