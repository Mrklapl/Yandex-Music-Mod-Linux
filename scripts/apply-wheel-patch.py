#!/usr/bin/env python3
import os, sys, glob, re

def patch_vibe_playerbar(inspect_dir):
    chunks_dir = os.path.join(inspect_dir, "app/_next/static/chunks")
    for fpath in glob.glob(os.path.join(chunks_dir, "*.js")):
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        # Check for 5.123.4 VibePlayerbar in 2850
        start_marker = 'let t9=(0,u.PA)(()=>{var e,t,i,a,n;let{experiments:r,sonataState:s,advert:o,settings:{isMobile:l}}=(0,U.g)()'
        end_marker = ';var t4=i(56530)'
        s_pos = content.find(start_marker)
        e_pos = content.find(end_marker, s_pos) if s_pos != -1 else -1

        if s_pos != -1 and e_pos != -1:
            print(f"Found modern VibePlayerBar in {os.path.basename(fpath)}")
            new_t9 = '''let t9=(0,u.PA)(()=>{var e,t,i,a,n;let{experiments:r,sonataState:s,advert:o,settings:{isMobile:l},fullscreenPlayer:fsp}=(0,U.g)(),{formatMessage:u}=(0,v.A)(),_=(0,ts.e)(),nav=(0,tm.N)(),b=s.entityMeta,p=!s.isPlaying&&s.isVibeContext,h=null!=(i=s.position)?i:0,x=null!=(a=s.duration)?a:0,[A,C]=(0,m.useState)(null),j=(0,m.useRef)(!1),{state:N,toggleTrue:P,toggleFalse:T}=(0,eo.e)(!1),k=!!x&&!s.isGenerativeContext&&N,S=j.current&&null!=A?A:h,w=x>0?Math.min(S,x)/x*100:0,I=(0,t1.E)(Math.round(S),Math.round(x)),E=(0,t1.E)(Math.round(x),Math.round(x)),O=(0,t2.P)(S),B=(0,t2.P)(x),[scrub,setScrub]=(0,m.useState)(null),dragRef=(0,m.useRef)({isDown:!1,isDragging:!1}),justScrubbedRef=(0,m.useRef)(!1);let onCenterPointerDown=(0,f.c)(e=>{if(0!==e.button||!x||x<=0)return;let target=e.currentTarget,rect=target.getBoundingClientRect();dragRef.current={isDown:!0,isDragging:!1,startX:e.clientX,startY:e.clientY,targetRect:rect,pointerId:e.pointerId,targetEl:target,lastSec:x>0?(h/x)*x:0};try{target.setPointerCapture(e.pointerId)}catch(t){}});let onCenterPointerMove=(0,f.c)(e=>{let drag=dragRef.current;if(!drag||!drag.isDown)return;let dx=e.clientX-drag.startX,dy=e.clientY-drag.startY;if(!drag.isDragging){if(Math.hypot(dx,dy)<4)return;drag.isDragging=!0}let rect=drag.targetRect,fraction=Math.max(0,Math.min(1,(e.clientX-rect.left)/rect.width)),curSec=fraction*x,fmt=e=>{let t=Math.max(0,Math.round(e)),a=Math.floor(t/60),i=t%60;return\"\"+a+\":\"+(i<10?\"0\":\"\")+i},text=fmt(curSec)+\" / \"+fmt(x),rawX=e.clientX-rect.left,minX=36,maxX=rect.width-36,tooltipX=Math.max(minX,Math.min(maxX,rawX));drag.lastSec=curSec,drag.lastRatio=fraction,setScrub({ratio:fraction,sec:curSec,tooltipX:tooltipX,text:text})});let onCenterPointerUp=(0,f.c)(e=>{let drag=dragRef.current;if(!drag||!drag.isDown)return;if(drag.isDragging){justScrubbedRef.current=!0;setTimeout(()=>{justScrubbedRef.current=!1},120);try{null==_||_.setProgress(drag.lastSec)}catch(t){}}try{drag.targetEl?.releasePointerCapture(drag.pointerId)}catch(t){}dragRef.current={isDown:!1,isDragging:!1};setScrub(null)});let onCenterPointerCancel=(0,f.c)(e=>{let drag=dragRef.current;if(drag?.isDown)try{drag.targetEl?.releasePointerCapture(drag.pointerId)}catch(t){}dragRef.current={isDown:!1,isDragging:!1};setScrub(null)});let onCenterClick=(0,f.c)(e=>{if(justScrubbedRef.current)return void(justScrubbedRef.current=!1);if(!b||s.isGenerativeContext||o.isAdvertShown)return;try{null==fsp||fsp.showFullscreenPlayerModal(),null==nav||nav({to:e8.AppScreen.PlayerScreen})}catch(t){}});let effRatio=scrub?scrub.ratio:x>0?Math.min(S,x)/x:0,effPercent=100*effRatio,M={\"--track-progress\":\"\".concat(effPercent,\"%\"),\"--progress-transition-duration\":(e=>{if(\"default\"!==e&&void 0!==e)return\"on1\"===e?\"150ms\":\"0ms\"})(null==(e=r.getExperiment(z.z.WebNextMainPlayerAnimation))?void 0:e.group),\"--progress-transition\":(j.current||scrub)?\"none\":void 0};let R=(0,m.useMemo)(()=>(0,tY.A)(()=>{T()},1e3),[T]),L=(0,f.c)((e,t)=>{o.isAdvertShown||(j.current=!t,l&&(P(),R.cancel(),R()),t?null==_||_.setProgress(e):C(e))}),W=(0,y.L)(()=>{if(s.isGenerativeContext)return(null==b?void 0:b.title)?(0,d.jsxs)(d.Fragment,{children:[(0,d.jsx)(\"span\",{className:t6().generativeIcon,children:(0,d.jsx)(Y.I,{size:\"xs\",variant:\"infinity\",\"data-test-id\":g.e8.player.VIBE_PLAYERBAR_NEUROMUSIC_ICON})}),(0,d.jsx)(\"span\",{className:t6().generativeTitle,children:b.title})]}):(0,d.jsx)(Y.I,{size:\"xs\",variant:\"infinity\",\"data-test-id\":g.e8.player.VIBE_PLAYERBAR_NEUROMUSIC_ICON});let e=[],t=[];return b&&(e.push((0,t0.X)(b.artists)),e.push(\"—\")),(null==b?void 0:b.title)&&t.push(b.title),!(null==b?void 0:b.isRemoved)&&(null==b?void 0:b.version)&&t.push(\"(\".concat(b.version,\")\")),(0,d.jsxs)(d.Fragment,{children:[e.length>0&&p&&(0,d.jsx)(\"span\",{className:t6().artists,children:e.join(\" \")}),t.join(\" \")]})});return(0,d.jsx)(\"div\",{className:t6().root,style:M,children:(0,d.jsxs)(\"div\",{className:(0,c.$)(t6().center,{[t6().center_withExplicitMark]:null==b?void 0:b.explicitDisclaimer,[t6().center_withExplicitMark_playing]:s.isPlaying,[t6().center_withoutExplicitMark]:!(null==b?void 0:b.explicitDisclaimer),[t6().center_withoutExplicitMark_playing]:s.isPlaying,[t6().center_withTimecode]:k||!!scrub,[t6().center_active]:!s.isGenerativeContext,VibePlayerbarMeta_scrubbing:!!scrub}),onMouseEnter:P,onMouseLeave:T,onClick:onCenterClick,onPointerDown:onCenterPointerDown,onPointerMove:onCenterPointerMove,onPointerUp:onCenterPointerUp,onPointerCancel:onCenterPointerCancel,style:scrub?{cursor:\"grabbing\",userSelect:\"none\"}:void 0,\"data-test-id\":g.e8.player.VIBE_PLAYERBAR_TIMECODE_SLIDER,children:[(0,d.jsx)(tQ,{className:t6().trackName,scrollingClassName:t6().scrollingTrackName,contentClassName:t6().trackNameText,pauseOnHover:!1,speed:35,gap:32,\"data-test-id\":g.e8.player.VIBE_PLAYERBAR_TRACK_NAME,children:W},\"\".concat(null!=(n=null==(t=s.entityMeta)?void 0:t.idWithContext)?n:\"default\",\"-\").concat(p)),(null==b?void 0:b.explicitDisclaimer)&&(0,d.jsx)(t8.N,{containerClassName:t6().explicitMarkContainer,getDescriptionTexts:b.getDescriptionTexts,size:\"xxxs\",variant:b.explicitDisclaimer,className:t6().explicitMark,trackId:b.id}),!s.isGenerativeContext&&(0,d.jsx)(\"span\",{className:t6().timecodeOverlay,\"aria-hidden\":!0,\"data-test-id\":g.e8.player.VIBE_PLAYERBAR_TIMECODE,children:scrub?scrub.text:\"\".concat(I,\" / \").concat(E)}),!s.isGenerativeContext&&(0,d.jsx)(tJ.A,{className:(0,c.$)(t6().slider,{[t6().slider_active]:!s.isGenerativeContext}),\"aria-label\":u({id:\"player-actions.timecode-control\"}),\"aria-valuetext\":scrub?scrub.text:\"\".concat(O,\" / \").concat(B),disabled:!b||o.isAdvertShown||!!scrub,style:{pointerEvents:\"none\"},onChange:L,onFocus:P,onBlur:T,maxValue:Math.round(x),mode:\"deferred\",value:Math.round(scrub?scrub.sec:S),showThumbVariant:\"never\",trackSize:\"s\",thumbSize:\"s\"}),scrub&&(0,d.jsx)(\"div\",{style:{position:\"absolute\",bottom:\"calc(100% + 12px)\",left:\"\".concat(scrub.tooltipX,\"px\"),transform:\"translateX(-50%)\",backgroundColor:\"rgba(22, 22, 26, 0.88)\",backdropFilter:\"blur(16px)\",WebkitBackdropFilter:\"blur(16px)\",color:\"#ffffff\",padding:\"4px 12px\",borderRadius:\"9999px\",fontSize:\"12px\",fontWeight:\"600\",fontVariantNumeric:\"tabular-nums\",pointerEvents:\"none\",zIndex:9999,boxShadow:\"0 4px 20px rgba(0, 0, 0, 0.4)\",whiteSpace:\"nowrap\",letterSpacing:\"0.2px\",lineHeight:\"1.4\"},children:scrub.text})]})})})'''
            content = content[:s_pos] + new_t9 + content[e_pos:]

            # Unrestrict reset button & settings
            t_target = '$=l.checkExperiment(z.z.WebNextDisableVibeSettings,"on")||b.isVibeStartRestricted||!u.isAuthorized'
            t_repl = '$=l.checkExperiment(z.z.WebNextDisableVibeSettings,"on")'
            if t_target in content:
                content = content.replace(t_target, t_repl, 1)

            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print("Successfully patched modern VibePlayerBar!")
            break

def patch_wheel_fallback(inspect_dir):
    chunks_dir = os.path.join(inspect_dir, "app/_next/static/chunks")
    for fpath in glob.glob(os.path.join(chunks_dir, "*.js")):
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        if "vibe-wheel.activity-wake-up" in content and "wheelNew" in content:
            print(f"Found modern Wheel Store in {os.path.basename(fpath)}")
            modified = False

            # 1. Resolve loadingState on pumpkin fallback
            target = 'else d.error("[Wheel] Load error",{error:t});e.loadingState=x.G.REJECT}})}})'
            new_code = 'else d.error("[Wheel] Load error",{error:t});e.loadingState=e.items.length>0?x.G.RESOLVE:x.G.REJECT}})}})'
            if target in content:
                content = content.replace(target, new_code)
                modified = True

            target_cond = 'catch(t){if(e.isEmpty&&a){'
            new_cond = 'catch(t){let fb=typeof a==="function"?a:(x=>x.id);if(e.isEmpty||0===e.items.length){'
            if target_cond in content:
                content = content.replace(target_cond, new_cond)
                modified = True

            target_call = '})(a);e.wheelId=i.wheelId'
            new_call = '})(fb);e.wheelId=i.wheelId'
            if target_call in content:
                content = content.replace(target_call, new_call)
                modified = True

            if modified:
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(content)
                print("Successfully patched modern Wheel fallback logic!")
            break

def patch_css(inspect_dir):
    css_dir = os.path.join(inspect_dir, "app/_next/static/css")
    for fpath in glob.glob(os.path.join(css_dir, "*.css")):
        with open(fpath, "r", encoding="utf-8") as f:
            css = f.read()

        if "VibePlayerbarMeta_center" in css:
            rule = '''
.VibePlayerbarMeta_center__6kbMi {
    user-select: none !important;
    -webkit-user-select: none !important;
}
.VibePlayerbarMeta_center__6kbMi.VibePlayerbarMeta_scrubbing:before {
    transition: none !important;
}
'''
            if '.VibePlayerbarMeta_scrubbing' not in css:
                css += rule
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(css)
                print(f"Successfully patched CSS in {os.path.basename(fpath)}!")
            else:
                print(f"CSS in {os.path.basename(fpath)} already patched.")
            break

def patch_modern_chunks(inspect_dir):
    chunks_dir = os.path.join(inspect_dir, "app/_next/static/chunks")
    for fname in os.listdir(chunks_dir):
        if not fname.endswith(".js"):
            continue
        fpath = os.path.join(chunks_dir, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        modified = False

        # Wheel Desktop fallback render
        target_render = "return l&&r?(0,i.jsx)(eS,{className:t}):(0,i.jsx)(L.RC,"
        new_render = "return(l||r||0===a.length)?(0,i.jsx)(eS,{className:t}):(0,i.jsx)(L.RC,"
        if target_render in content:
            content = content.replace(target_render, new_render)
            modified = True
            print(f"Patched wheel desktop render in {fname}")

        # Plus unlock: User.hasPlus -> true
        target_has_plus = "get hasPlus(){return!!e.account.data.hasPlus}"
        new_has_plus = "get hasPlus(){return!0}"
        if target_has_plus in content:
            content = content.replace(target_has_plus, new_has_plus)
            modified = True
            print(f"Patched User.hasPlus in {fname}")

        # Plus unlock: FreeAccess -> false
        target_free_access = 'FreeAccess").views(e=>{let t={get isFreeDesktopUser(){let{user:t}=(0,P.M)(e);return!t.hasPlus&&T.NN},get isFreeWebUser(){let{user:t}=(0,P.M)(e);return!t.hasPlus&&T.$3},get isFreeUser(){return t.isFreeDesktopUser||t.isFreeWebUser},get isFreePlaybackDisabled(){'
        new_free_access = 'FreeAccess").views(e=>{let t={get isFreeDesktopUser(){return!1},get isFreeWebUser(){return!1},get isFreeUser(){return!1},get isFreePlaybackDisabled(){return!1;'
        if target_free_access in content:
            content = content.replace(target_free_access, new_free_access)
            modified = True
            print(f"Patched FreeAccess in {fname}")

        # Plus unlock: e.account.data hasPlus -> true
        target_acct_plus = "hasPlus:e.hasPlus,publicId:e.publicId"
        new_acct_plus = "hasPlus:!0,publicId:e.publicId"
        if target_acct_plus in content:
            content = content.replace(target_acct_plus, new_acct_plus)
            modified = True
            print(f"Patched e.account.data.hasPlus in {fname}")

        # Plus unlock: Bypass PREVIEW quality fallback
        target_preview = "if(!h.isAuthorized||f.isFreeDesktopUser||H||f.limitedFreePlayback)return tV.e.PREVIEW;"
        new_preview = "if(!1)return tV.e.PREVIEW;"
        if target_preview in content:
            content = content.replace(target_preview, new_preview)
            modified = True
            print(f"Patched PREVIEW quality check in {fname}")

        if modified:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)

if __name__ == "__main__":
    inspect_dir = sys.argv[1] if len(sys.argv) > 1 else "inspect_asar"
    if not os.path.isdir(inspect_dir):
        if os.path.isdir(os.path.join("..", inspect_dir)):
            inspect_dir = os.path.join("..", inspect_dir)
        else:
            print(f"ERROR: {inspect_dir} not found!")
            sys.exit(1)
    print(f"Applying patches to: {inspect_dir}")
    patch_vibe_playerbar(inspect_dir)
    patch_wheel_fallback(inspect_dir)
    patch_modern_chunks(inspect_dir)
    patch_css(inspect_dir)
    print("All patches applied successfully!")
