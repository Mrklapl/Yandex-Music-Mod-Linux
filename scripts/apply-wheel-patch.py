import os, sys

def patch_7511(inspect_dir):
    path = os.path.join(inspect_dir, "app/_next/static/chunks/7511-470ddb0b1430b7fa.js")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Locate getData in module 35796
    target_start = "getData:(0,r.L3)(function*(n,l){let{context:d}=n"
    if target_start not in content:
        print("ERROR: target_start not found in 7511!")
        sys.exit(1)
        
    start_pos = content.find(target_start)
    end_marker = "}),S=n.default.default"
    end_pos = content.find(end_marker, start_pos)
    if end_pos == -1:
        print("ERROR: end_marker not found in 7511!")
        sys.exit(1)
        
    # Clean getData block without forcing genre:all, perfectly balanced syntax
    new_block = """getData:(0,r.L3)(function*(n,l){let{context:d}=n;let u=(e=>{switch(e.type){case s.b.ALBUM:case s.b.ARTIST:return"".concat(e.type,":").concat(e.data.id);case s.b.PLAYLIST:return"".concat(e.type,":").concat(e.data.playlistUuid);case s.b.WAVE:return"".concat(e.type,":").concat(e.data.seeds.join(","));case s.b.GENERATIVE:case s.b.CLIP:return e.type;case s.b.OTHER:return"".concat(e.type,":").concat(e.data?.id??"")}})(d);if(u===e.lastRequestId&&e.items.length>0)return;let{wheelResource:m,modelActionsLogger:_}=(0,r._$)(e);e.loadingState=o.GuX.PENDING;let y=(()=>{if(0===i)return[];let e=Array(i),n=(a-i+100)%100;for(let a=0;a<i;a++){let i=t[(n+a)%100];i&&(e[a]=i)}return e})();let fbFn=e=>{let t=(e||(x=>x.id))({id:"vibe-wheel.activity-description"}),a=(e||(x=>x.id))({id:"vibe-wheel.mood-description"});return{wheelId:"PUMPKIN",items:[{id:"activity:wake-up",type:c.D.WAVE,data:{wave:{name:(e||(x=>x.id))({id:"vibe-wheel.activity-wake-up"}),description:t,seeds:["activity:wake-up"]},agent:{animationUri:"https://music-custom-wave-media.music.yandex.net/JVsyUlrs9Y",cover:{uri:"https://avatars.mds.yandex.net/get-music-misc/28592/rotor-activity-wake-up-agent-cover-RSUMc/%%",color:"#FFFFD6"}}}},{id:"activity:road-trip",type:c.D.WAVE,data:{wave:{name:(e||(x=>x.id))({id:"vibe-wheel.activity-road-trip"}),description:t,seeds:["activity:road-trip"]},agent:{animationUri:"https://music-custom-wave-media.music.yandex.net/Foah9sRLsS",cover:{uri:"https://avatars.mds.yandex.net/get-music-misc/70683/rotor-activity-road-trip-agent-cover-S1vPp/%%",color:"#FFFFDF"}}}},{id:"activity:work-background",type:c.D.WAVE,data:{wave:{name:(e||(x=>x.id))({id:"vibe-wheel.activity-work-background"}),description:t,seeds:["activity:work-background"]},agent:{animationUri:"https://music-custom-wave-media.music.yandex.net/tsXpFHIBjM",cover:{uri:"https://avatars.mds.yandex.net/get-music-misc/2413828/rotor-activity-work-background-agent-cover-5t6qb/%%",color:"#FFFFFF"}}}},{id:"activity:workout",type:c.D.WAVE,data:{wave:{name:(e||(x=>x.id))({id:"vibe-wheel.activity-workout"}),description:t,seeds:["activity:workout"]},agent:{animationUri:"https://music-custom-wave-media.music.yandex.net/PexWCCcEc9",cover:{uri:"https://avatars.mds.yandex.net/get-music-misc/2413828/rotor-activity-workout-agent-cover-Wcrjo/%%",color:"#EBFFFE"}}}},{id:"activity:fall-asleep",type:c.D.WAVE,data:{wave:{name:(e||(x=>x.id))({id:"vibe-wheel.activity-fall-asleep"}),description:t,seeds:["activity:fall-asleep"]},agent:{animationUri:"https://music-custom-wave-media.music.yandex.net/J9QAoYnnPe",cover:{uri:"https://avatars.mds.yandex.net/get-music-misc/28592/rotor-activity-fall-asleep-agent-cover-XaOnj/%%",color:"#FAFFFF"}}}},{id:"mood:energetic",type:c.D.WAVE,data:{wave:{name:(e||(x=>x.id))({id:"vibe-wheel.mood-energetic"}),description:a,seeds:["mood:energetic"]},agent:{animationUri:"https://music-custom-wave-media.music.yandex.net/e6Ptlara08",cover:{uri:"https://avatars.mds.yandex.net/get-music-misc/70683/rotor-mood-energetic-agent-cover-NrJtV/%%",color:"#FDFAFF"}}}},{id:"mood:happy",type:c.D.WAVE,data:{wave:{name:(e||(x=>x.id))({id:"vibe-wheel.mood-happy"}),description:a,seeds:["mood:happy"]},agent:{animationUri:"https://music-custom-wave-media.music.yandex.net/EzOBeQmIXi",cover:{uri:"https://avatars.mds.yandex.net/get-music-misc/70683/rotor-mood-happy-agent-cover-JWFjr/%%",color:"#FFFFE8"}}}},{id:"mood:sad",type:c.D.WAVE,data:{wave:{name:(e||(x=>x.id))({id:"vibe-wheel.mood-sad"}),description:a,seeds:["mood:sad"]},agent:{animationUri:"https://music-custom-wave-media.music.yandex.net/rrF2I4tUvZ",cover:{uri:"https://avatars.mds.yandex.net/get-music-misc/30221/rotor-mood-sad-agent-cover-IN0O6/%%",color:"#EAFFFF"}}}}]};};try{let t=yield m.wheelNew({context:d,feedbacks:y});let parsed=p(t);if(parsed&&parsed.length>0){i=0,e.wheelId=t.wheelId,e.items=(0,r.wg)(parsed),e.activeIndex=1,e.lastRequestId=u,e.loadingState=o.GuX.RESOLVE}else if(e.items.length===0){let fb=fbFn(l);e.wheelId=fb.wheelId,e.items=(0,r.wg)(p(fb)),e.activeIndex=1,e.lastRequestId=u,e.loadingState=o.GuX.RESOLVE}else{e.loadingState=o.GuX.RESOLVE}}catch(t){if(_.error(t),e.isEmpty){let fb=fbFn(l);e.wheelId=fb.wheelId,e.items=(0,r.wg)(p(fb)),e.activeIndex=1}e.loadingState=o.GuX.RESOLVE}})}"""
    
    content = content[:start_pos] + new_block + content[end_pos:]
    
    # 2. Fix null-safe addFeedback calls to prevent Uncaught TypeError in detached items
    target_fb_view = "handleFeedbackView(){let{wheel:t}=(0,r.Zn)(e);t.addFeedback(i.VIEW,e.type,e.id,e.index)}"
    safe_fb_view = "handleFeedbackView(){let t=(0,r.Zn)(e);(t?.wheel||t)?.addFeedback?.(i.VIEW,e.type,e.id,e.index)}"
    if target_fb_view in content:
        content = content.replace(target_fb_view, safe_fb_view)
        
    target_fb_click = "handleFeedbackClick(){let{wheel:t}=(0,r.Zn)(e);t.addFeedback(i.CLICK,e.type,e.id,e.index)}"
    safe_fb_click = "handleFeedbackClick(){let t=(0,r.Zn)(e);(t?.wheel||t)?.addFeedback?.(i.CLICK,e.type,e.id,e.index)}"
    if target_fb_click in content:
        content = content.replace(target_fb_click, safe_fb_click)
        
    # 3. Add PROMO support to enum module 58412 (used by BaseWheelItem style validation)
    target_enum = 'e.DEFAULT="DEFAULT",e.CONTROL="CONTROL",e.CONTROL_ACCENT="CONTROL_ACCENT"'
    new_enum = 'e.DEFAULT="DEFAULT",e.CONTROL="CONTROL",e.CONTROL_ACCENT="CONTROL_ACCENT",e.PROMO="PROMO"'
    if target_enum in content:
        content = content.replace(target_enum, new_enum)
        
    # 4. Normalize style fallback in module 35796 p function
    target_p_style = "style:e.style??d.y.DEFAULT"
    new_p_style = "style:(e.style&&Object.values(d.y).includes(e.style))?e.style:d.y.DEFAULT"
    if target_p_style in content:
        content = content.replace(target_p_style, new_p_style)
        
    # 5. Reset button logic fix: Only show 'Назад к привычному' when actually in a custom interest/modifier
    target_reset_avail = 'f=(()=>{let e=(0,P.eGp)(),t=e?.state.currentContext.value;if(t?.data.type===K.K.Vibe){var a;let e=t.data.meta.session?.wave;if(1===e?.seeds.length&&e?.seeds[0]===P.M19||1===e?.seeds.length&&(null==e||null==(a=e.seeds[0])?void 0:a.includes(P.yxZ)))return!1}return!0})()'
    new_reset_avail = 'f=(()=>{try{if(d?.isMyVibe)return!1;let mv=g({id:\"entity-names.my-vibe\"});if(b===mv)return!1;let e=(0,P.eGp)(),t=e?.state.currentContext.value;if(!t||t?.data?.type!==K.K.Vibe)return!1;let w=t?.data?.meta?.session?.wave;if(!w||!w.seeds||0===w.seeds.length)return!1;if(w.seeds.includes(P.M19)||w.seeds[0]===P.M19||w.seeds.some(e=>e&&e.includes(P.yxZ)))return!1;return!0}catch(e){return!1}})()'
    if target_reset_avail in content:
        content = content.replace(target_reset_avail, new_reset_avail, 1)

    # 6. VibePlayerBar seeking/scrubbing gesture: click & drag to scrub with floating timecode badge
    pos2 = content.find('let Ii=')
    end2 = content.find('var Li=', pos2) if pos2 != -1 else -1
    if pos2 != -1 and end2 != -1:
        orig_Ii = content[pos2:end2]
        if 'onCenterPointerDown' not in orig_Ii:
            new_Ii = '''let Ii=(0,d.PA)(e=>{let{hoveredButtonClassName:t}=e,{sonataState:a,advert:i,fullscreenPlayer:r,settings:{isMobile:s}}=(0,n.Pjs)(),o=(0,n.eGp)(),{formatMessage:d}=(0,re.A)(),m=(0,n.zwV)(),p=(0,N.d0)(),{isLiked:_,handleLike:y,isDisliked:h,handleDislike:g}=Ra(),x=(0,n.NKK)(),b=a.entityMeta,f=b?.mainAlbum,C=!a.isPlaying&&a.isVibeContext,k=a.position??0,S=a.duration??0,P=!a.isPlaying&&!b,[scrub,setScrub]=(0,u.useState)(null),dragRef=(0,u.useRef)({isDown:!1,isDragging:!1}),justScrubbedRef=(0,u.useRef)(!1);let onCenterPointerDown=(0,xe.c)(e=>{if(0!==e.button||!S||S<=0)return;let target=e.currentTarget,rect=target.getBoundingClientRect(),progressEl=target.closest(\".\"+ji().progress)||target.parentElement,progRect=progressEl?progressEl.getBoundingClientRect():rect;dragRef.current={isDown:!0,isDragging:!1,startX:e.clientX,startY:e.clientY,targetRect:rect,progRect:progRect,pointerId:e.pointerId,targetEl:target,lastSec:S>0?(k/S)*S:0};try{target.setPointerCapture(e.pointerId)}catch(t){}});let onCenterPointerMove=(0,xe.c)(e=>{let drag=dragRef.current;if(!drag||!drag.isDown)return;let dx=e.clientX-drag.startX,dy=e.clientY-drag.startY;if(!drag.isDragging){if(Math.hypot(dx,dy)<4)return;drag.isDragging=!0}let rect=drag.targetRect,progRect=drag.progRect,fraction=Math.max(0,Math.min(1,(e.clientX-rect.left)/rect.width)),curSec=fraction*S,fmt=e=>{let t=Math.max(0,Math.round(e)),a=Math.floor(t/60),i=t%60;return\"\"+a+\":\"+(i<10?\"0\":\"\")+i},text=fmt(curSec)+\" / \"+fmt(S),rawX=e.clientX-progRect.left,minX=rect.left-progRect.left+36,maxX=rect.right-progRect.left-36,tooltipX=Math.max(minX,Math.min(maxX,rawX));drag.lastSec=curSec,drag.lastRatio=fraction,setScrub({ratio:fraction,sec:curSec,tooltipX:tooltipX,text:text})});let onCenterPointerUp=(0,xe.c)(e=>{let drag=dragRef.current;if(!drag||!drag.isDown)return;if(drag.isDragging){justScrubbedRef.current=!0,setTimeout(()=>{justScrubbedRef.current=!1},120);try{null==o||o.setProgress(drag.lastSec)}catch(t){}}try{drag.targetEl?.releasePointerCapture(drag.pointerId)}catch(t){}(dragRef.current={isDown:!1,isDragging:!1}),setScrub(null)});let onCenterPointerCancel=(0,xe.c)(e=>{let drag=dragRef.current;if(drag?.isDown)try{drag.targetEl?.releasePointerCapture(drag.pointerId)}catch(t){}(dragRef.current={isDown:!1,isDragging:!1}),setScrub(null)});let w=(0,xe.c)(()=>{if(a.entityMeta){if(r.modal.isOpened)return void r.modal.close();r.modal.open()}});(0,u.useEffect)(()=>{if(!a.isGenerativeContext)return null==m||m.addShortcutsListener(n.Mo.MAIN,n.lbr.TOGGLE_FULLSCREEN_PLAYER,w),null==m||m.addShortcutsListener(n.Mo.MAIN,n.lbr.LIKE,y),null==m||m.addShortcutsListener(n.Mo.MAIN,n.lbr.DISLIKE,g),()=>{null==m||m.removeShortcutsListener(n.Mo.MAIN,n.lbr.TOGGLE_FULLSCREEN_PLAYER),null==m||m.removeShortcutsListener(n.Mo.MAIN,n.lbr.LIKE),null==m||m.removeShortcutsListener(n.Mo.MAIN,n.lbr.DISLIKE)}},[g,y,m,a.isGenerativeContext,a.entityMeta,w]),(0,u.useEffect)(()=>{let e=b?.id,t=null!=b&&!1===b.hasSyncLyrics,a=null!=b&&!0===b.hasSyncLyrics,i=b?.trackSource,n=!!b?.isNonMusic,s=!0;try{!1===(\"undefined\"!=typeof window&&window.nativeSettings?window.nativeSettings.get(\"modSettings.lrclib.useText\"):null)&&(s=!1)}catch(e){}let l=e&&r.syncLyrics.currentTrackId!==e&&(t||a||!!b?.hasLyrics||\"UGC\"===i||!n&&s),c=J(o);G=o,l&&r.syncLyrics.getData(e),r.syncLyrics.prefetchTrack(c)},[b?.id,b?.hasSyncLyrics,b?.hasLyrics,b?.trackSource,b?.isNonMusic,r.syncLyrics,o]);let j=(0,Ne.L)(()=>{if(a.isGenerativeContext)return(0,l.jsx)(oe.Icon,{size:\"xs\",variant:\"infinity\"});let e=[];return C&&b&&(e.push((0,gi.XV)(b.artists)),e.push(\" — \")),b?.title&&e.push(b.title),!b?.isRemoved&&b?.version&&e.push(\"(\".concat(b.version,\")\")),e.join(\" \")}),I=(0,xe.c)(()=>{!b||a.isGenerativeContext||i.isAdvertShown||(r.showFullscreenPlayerModal(),x({to:ua.QT.PlayerScreen}))}),onCenterClick=(0,xe.c)(e=>{if(justScrubbedRef.current)return void(justScrubbedRef.current=!1);I()}),L=(0,xe.c)(e=>{(e.code===n.vLr.SPACE||e.code===n.vLr.ENTER)&&(e.preventDefault(),onCenterClick())}),T=(0,xe.c)(async e=>{await p(a,e)}),effectiveRatio=scrub?scrub.ratio:S>0?Math.min(k,S)/S:0,effectivePercent=100*effectiveRatio,E={\"--track-progress\":\"\".concat(effectivePercent,\"%\"),...(scrub?{\"--track-progress-transition\":\"none\"}:{})};return(0,l.jsxs)(\"section\",{role:\"region\",\"aria-label\":d({id:\"a11y-regions.player\"}),className:ji().root,style:E,children:[(0,l.jsx)(Ci,{album:f,hoveredButtonClassName:t}),(0,l.jsxs)(\"div\",{className:(0,c.$)(ji().progress,{[ji().progress_visible]:!P}),style:E,children:[!s&&(0,l.jsx)(Ya.r,{className:ji().changeVolume,buttonClassName:ji().button,verticalSliderClassName:ji().verticalSlider,variant:Ya.q.VERTICAL,sonataVolume:a.volume,onVolumeSet:a.setVolume,onVolumeClick:T}),(0,l.jsx)(v._I,{className:ji().button,disabled:!b||i.isAdvertShown,isDisliked:h,onClick:g,iconSize:\"xs\"}),(0,l.jsxs)(\"div\",{className:(0,c.$)(ji().center,{[ji().center_withExplicitMark]:b?.explicitDisclaimer,VibePlayerBar_scrubbing:!!scrub}),onClick:onCenterClick,onKeyDown:L,onPointerDown:onCenterPointerDown,onPointerMove:onCenterPointerMove,onPointerUp:onCenterPointerUp,onPointerCancel:onCenterPointerCancel,role:\"button\",tabIndex:0,\"aria-label\":d({id:\"player-actions.fullscreen-button\"}),style:scrub?{cursor:\"grabbing\",userSelect:\"none\"}:void 0,children:[(0,l.jsx)(vi,{className:ji().trackName,scrollingClassName:ji().scrollingTrackName,contentClassName:ji().trackNameText,pauseOnHover:!1,speed:35,gap:32,children:j},\"\".concat(a.entityMeta?.idWithContext??\"default\",\"-\").concat(C)),b?.explicitDisclaimer&&(0,l.jsx)(v.Nq,{containerClassName:ji().explicitMarkContainer,getDescriptionTexts:b.getDescriptionTexts,size:\"xxxs\",variant:b.explicitDisclaimer,className:ji().explicitMark,trackId:b.id})]}),(0,l.jsx)(v.cy,{className:ji().button,disabled:!b||i.isAdvertShown,isLiked:_,onClick:y,iconSize:\"xs\"}),!s&&(0,l.jsx)(Pi,{buttonClassName:(0,c.$)(ji().button,ji().important)}),(0,l.jsx)(Wa,{}),scrub&&(0,l.jsx)(\"div\",{style:{position:\"absolute\",bottom:\"calc(100% + 12px)\",left:\"\".concat(scrub.tooltipX,\"px\"),transform:\"translateX(-50%)\",backgroundColor:\"rgba(22, 22, 26, 0.88)\",backdropFilter:\"blur(16px)\",WebkitBackdropFilter:\"blur(16px)\",color:\"#ffffff\",padding:\"4px 12px\",borderRadius:\"9999px\",fontSize:\"12px\",fontWeight:\"600\",fontVariantNumeric:\"tabular-nums\",pointerEvents:\"none\",zIndex:9999,boxShadow:\"0 4px 20px rgba(0, 0, 0, 0.4)\",whiteSpace:\"nowrap\",letterSpacing:\"0.2px\",lineHeight:\"1.4\"},children:scrub.text})]})]})});'''
            content = content[:pos2] + new_Ii + content[end2:]

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully patched 7511!")

def patch_css(inspect_dir):
    path = os.path.join(inspect_dir, "app/_next/static/css/9efcd640c6a02026.css")
    if not os.path.exists(path):
        print(f"Warning: {path} not found")
        return
    with open(path, "r", encoding="utf-8") as f:
        css = f.read()
    rule = '''
.VibePlayerBar_center__yug8i {
    user-select: none !important;
    -webkit-user-select: none !important;
}
.VibePlayerBar_center__yug8i.VibePlayerBar_scrubbing:before {
    transition: none !important;
}
'''
    if '.VibePlayerBar_scrubbing' not in css:
        css += rule
        with open(path, "w", encoding="utf-8") as f:
            f.write(css)
        print("Successfully patched 9efcd640c6a02026.css!")
    else:
        print("CSS already patched!")

def patch_6602(inspect_dir):
    path = os.path.join(inspect_dir, "app/_next/static/chunks/6602.3894c4c5abbbd85d.js")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Desktop render fallback so it never collapses to empty
    target_render = "return l&&r?(0,a.jsx)(H,{className:t}):(0,a.jsx)(v.RC,"
    new_render = "return(l||r||0===i.length)?(0,a.jsx)(H,{className:t}):(0,a.jsx)(v.RC,"
    if target_render in content:
        content = content.replace(target_render, new_render)
    
    # 2. In entity change listener b: restore genuine seeds (remove genre:all hack)
    hack_case_vibe = 'case _.K.Vibe:{let sd=String(d).split(",");if(sd.length===1&&sd[0]==="user:onyourwave")sd=["user:onyourwave","genre:all"];return{type:h.b.WAVE,data:{seeds:sd}}};'
    clean_case_vibe = 'case _.K.Vibe:return{type:h.b.WAVE,data:{seeds:String(d).split(",")}};'
    if hack_case_vibe in content:
        content = content.replace(hack_case_vibe, clean_case_vibe)
    
    # 3. Clean any illegal hook calls in G
    bad_effects = [
        ';(0,s.useEffect)(()=>{if(0===i.length){(0,c.Pjs)().wheel.getData({context:{type:h.b.WAVE,data:{seeds:["user:onyourwave"]}}},_)}},[i.length]);',
        '(0,s.useEffect)(()=>{if(0===i.length){(0,c.Pjs)().wheel.getData({context:{type:h.b.WAVE,data:{seeds:["user:onyourwave"]}}},_)}},[i.length]);',
        ';(0,s.useEffect)(()=>{if(0===i.length){(0,c.Pjs)().wheel.getData({context:{type:h.b.WAVE,data:{seeds:["user:onyourwave","genre:all"]}}},_)}},[i.length]);',
        '(0,s.useEffect)(()=>{if(0===i.length){(0,c.Pjs)().wheel.getData({context:{type:h.b.WAVE,data:{seeds:["user:onyourwave","genre:all"]}}},_)}},[i.length]);'
    ]
    for b in bad_effects:
        content = content.replace(b, "")
    
    # Ensure semicolon after slideToLoop effect closing parenthesis before let j
    content = content.replace("},[o,i.length])let j=", "},[o,i.length]);let j=")
    content = content.replace("},[o,i.length]),let j=", "},[o,i.length]);let j=")
    
    # 4. In he: add safe on-mount check to trigger wheel fetch if empty
    target_he_effect = '(0,s.useEffect)(()=>{let e=p?.state.queueState.currentEntity.onChange(b);return()=>{null==e||e()}},[p,b,i])'
    new_he_effect = '(0,s.useEffect)(()=>{if(i.isEmpty){let cur=p?.state?.queueState?.currentEntity?.value;cur?b(cur):i.getData({context:{type:h.b.WAVE,data:{seeds:["user:onyourwave"]}}})}let e=p?.state.queueState.currentEntity.onChange(b);return()=>{null==e||e()}},[p,b,i])'
    if target_he_effect in content:
        content = content.replace(target_he_effect, new_he_effect)
    
    # 5. getData call condition in b: allow getData if isEmpty
    target_call = "(i.entityMeta?.isTrackMusic||!t.lastRequestId)&&t.getData({context:l},e)"
    new_call = "(i.entityMeta?.isTrackMusic||!t.lastRequestId||t.isEmpty)&&t.getData({context:l},e)"
    if target_call in content:
        content = content.replace(target_call, new_call)
        
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully patched 6602!")

def patch_modern_chunks(inspect_dir):
    chunks_dir = os.path.join(inspect_dir, "app/_next/static/chunks")
    if not os.path.isdir(chunks_dir):
        return
    for fname in os.listdir(chunks_dir):
        if not fname.endswith(".js"):
            continue
        fpath = os.path.join(chunks_dir, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        modified = False

        # 1. Reset button logic fix for modern build:
        target_reset = "$=(()=>{let e=(0,ts.e)(),t=null==e?void 0:e.state.currentContext.value;if((null==t?void 0:t.data.type)===iP.K.Vibe){var i,a;let e=null==(i=t.data.meta.session)?void 0:i.wave;if((null==e?void 0:e.seeds.length)===1&&(null==e?void 0:e.seeds[0])===eu.M1||(null==e?void 0:e.seeds.length)===1&&(null==e||null==(a=e.seeds[0])?void 0:a.includes(eu.yx)))return!1}return!0})()"
        new_reset = "$=(()=>{try{let e=(0,ts.e)(),t=e?.state.currentContext.value;if(!t||t?.data?.type!==iP.K.Vibe)return!1;let w=t?.data?.meta?.session?.wave;if(!w||!w.seeds||0===w.seeds.length)return!1;if(w.seeds.includes(eu.M1)||w.seeds[0]===eu.M1||w.seeds.some(e=>e&&e.includes(eu.yx)))return!1;return!0}catch(e){return!1}})()"
        if target_reset in content:
            content = content.replace(target_reset, new_reset)
            modified = True
            print(f"Patched reset button logic in modern chunk: {fname}")

        # 2. Wheel fallback render in modern build:
        target_render = "return l&&r?(0,i.jsx)(eS,{className:t}):(0,i.jsx)(L.RC,"
        new_render = "return(l||r||0===a.length)?(0,i.jsx)(eS,{className:t}):(0,i.jsx)(L.RC,"
        if target_render in content:
            content = content.replace(target_render, new_render)
            modified = True
            print(f"Patched wheel fallback in modern chunk: {fname}")

        if modified:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)

if __name__ == "__main__":
    inspect_dir = sys.argv[1] if len(sys.argv) > 1 else "inspect_asar"
    if not os.path.isdir(inspect_dir):
        # Check parent directory
        if os.path.isdir(os.path.join("..", inspect_dir)):
            inspect_dir = os.path.join("..", inspect_dir)
        else:
            print(f"ERROR: {inspect_dir} not found!")
            sys.exit(1)
    print(f"Applying wheel patch to: {inspect_dir}")
    if os.path.exists(os.path.join(inspect_dir, "app/_next/static/chunks/7511-470ddb0b1430b7fa.js")):
        patch_7511(inspect_dir)
    if os.path.exists(os.path.join(inspect_dir, "app/_next/static/chunks/6602.3894c4c5abbbd85d.js")):
        patch_6602(inspect_dir)
    patch_modern_chunks(inspect_dir)
    patch_css(inspect_dir)
    print("All patches applied successfully!")
