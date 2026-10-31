#!/usr/bin/env python3
import os, sys, glob, re

def patch_vibe_playerbar(inspect_dir):
    chunks_dir = os.path.join(inspect_dir, "app/_next/static/chunks")
    for fpath in glob.glob(os.path.join(chunks_dir, "*.js")):
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. Check for 5.125.x VibePlayerbar
        start_125 = 'it=(0,u.PA)(e=>{var t,i,n,a,r;let{shouldShowArtists:s,shouldShowArtistsWithTrackTitle:o,shouldKeepMobileSpacingOnPause:l}=e,{experiments:u,sonataState:_,advert:v,settings:{isMobile:p}}=(0,U.g)()'
        end_125 = ';var ii=i(19376)'
        s125 = content.find(start_125)
        e125 = content.find(end_125, s125) if s125 != -1 else -1

        if s125 != -1 and e125 != -1:
            print(f"Found 5.125+ VibePlayerBar in {os.path.basename(fpath)}")
            new_it = '''it=(0,u.PA)(e=>{var t,i,n,a,r;let{shouldShowArtists:s,shouldShowArtistsWithTrackTitle:o,shouldKeepMobileSpacingOnPause:l}=e,{experiments:u,sonataState:_,advert:v,settings:{isMobile:p},fullscreenPlayer:fsp}=(0,U.g)(),{formatMessage:h}=(0,b.A)(),x=(0,ts.e)(),nav=(0,tp.N)(),y=_.entityMeta,C=null!=(n=_.position)?n:0,j=null!=(a=_.duration)?a:0,[k,N]=(0,m.useState)(null),T=(0,m.useRef)(!1),{state:P,toggleTrue:I,toggleFalse:S}=(0,eo.e)(!1),E=!!j&&!_.isGenerativeContext&&P,w=T.current&&null!=k?k:C,B=j>0?Math.min(w,j)/j*100:0,O=(0,t$.E)(Math.round(w),Math.round(j)),M=(0,t$.E)(Math.round(j),Math.round(j)),R=(0,tZ.P)(w),L=(0,tZ.P)(j),[scrub,setScrub]=(0,m.useState)(null),dragRef=(0,m.useRef)({isDown:!1,isDragging:!1}),justScrubbedRef=(0,m.useRef)(!1);let onCenterPointerDown=(0,f.c)(e=>{if(0!==e.button||!j||j<=0)return;let target=e.currentTarget,rect=target.getBoundingClientRect();dragRef.current={isDown:!0,isDragging:!1,startX:e.clientX,startY:e.clientY,targetRect:rect,pointerId:e.pointerId,targetEl:target,lastSec:j>0?(C/j)*j:0};try{target.setPointerCapture(e.pointerId)}catch(t){}});let onCenterPointerMove=(0,f.c)(e=>{let drag=dragRef.current;if(!drag||!drag.isDown)return;let dx=e.clientX-drag.startX,dy=e.clientY-drag.startY;if(!drag.isDragging){if(Math.hypot(dx,dy)<4)return;drag.isDragging=!0}let rect=drag.targetRect,fraction=Math.max(0,Math.min(1,(e.clientX-rect.left)/rect.width)),curSec=fraction*j,fmt=e=>{let t=Math.max(0,Math.round(e)),a=Math.floor(t/60),i=t%60;return\"\"+a+\":\"+(i<10?\"0\":\"\")+i},text=fmt(curSec)+\" / \"+fmt(j),rawX=e.clientX-rect.left,minX=36,maxX=rect.width-36,tooltipX=Math.max(minX,Math.min(maxX,rawX));drag.lastSec=curSec,drag.lastRatio=fraction,setScrub({ratio:fraction,sec:curSec,tooltipX:tooltipX,text:text})});let onCenterPointerUp=(0,f.c)(e=>{let drag=dragRef.current;if(!drag||!drag.isDown)return;if(drag.isDragging){justScrubbedRef.current=!0;setTimeout(()=>{justScrubbedRef.current=!1},120);try{null==x||x.setProgress(drag.lastSec)}catch(t){}}try{drag.targetEl?.releasePointerCapture(drag.pointerId)}catch(t){}dragRef.current={isDown:!1,isDragging:!1};setScrub(null)});let onCenterPointerCancel=(0,f.c)(e=>{let drag=dragRef.current;if(drag?.isDown)try{drag.targetEl?.releasePointerCapture(drag.pointerId)}catch(t){}dragRef.current={isDown:!1,isDragging:!1};setScrub(null)});let onCenterClick=(0,f.c)(e=>{if(justScrubbedRef.current)return void(justScrubbedRef.current=!1);if(!y||_.isGenerativeContext||v.isAdvertShown)return;try{null==fsp||fsp.showFullscreenPlayerModal(),null==nav||nav({to:e5.AppScreen.PlayerScreen})}catch(t){}});let effRatio=scrub?scrub.ratio:j>0?Math.min(w,j)/j:0,effPercent=100*effRatio,V={\"--track-progress\":\"\".concat(effPercent,\"%\"),\"--progress-transition-duration\":(e=>{if(\"default\"!==e&&void 0!==e)return\"on1\"===e?\"150ms\":\"0ms\"})(null==(t=u.getExperiment(z.z.WebNextMainPlayerAnimation))?void 0:t.group),\"--progress-transition\":(T.current||scrub)?\"none\":void 0};let D=(0,m.useMemo)(()=>(0,tY.A)(()=>{S()},1e3),[S]),W=(0,f.c)((e,t)=>{v.isAdvertShown||(T.current=!t,p&&(I(),D.cancel(),D()),t?null==x||x.setProgress(e):N(e))}),F=(0,A.L)(()=>{if(_.isGenerativeContext)return(null==y?void 0:y.title)?(0,c.jsxs)(c.Fragment,{children:[(0,c.jsx)(\"span\",{className:t0().generativeIcon,children:(0,c.jsx)(Y.I,{size:\"xs\",variant:\"infinity\",\"data-test-id\":g.e8.player.VIBE_PLAYERBAR_NEUROMUSIC_ICON})}),(0,c.jsx)(\"span\",{className:t0().generativeTitle,children:y.title})]}):(0,c.jsx)(Y.I,{size:\"xs\",variant:\"infinity\",\"data-test-id\":g.e8.player.VIBE_PLAYERBAR_NEUROMUSIC_ICON});let e=[],t=[];return y&&(e.push((0,tG.X)(y.artists)),e.push(\"—\")),(null==y?void 0:y.title)&&t.push(y.title),!(null==y?void 0:y.isRemoved)&&(null==y?void 0:y.version)&&t.push(\"(\".concat(y.version,\")\")),(0,c.jsxs)(c.Fragment,{children:[e.length>0&&(s||o)&&(0,c.jsx)(\"span\",{className:(0,d.$)(t0().artists,{[t0().artists_hidden]:!s,[t0().artists_visibleOnCompact]:o}),children:e.join(\" \")}),t.join(\" \")]})});return(0,c.jsx)(\"div\",{className:t0().root,style:V,children:(0,c.jsxs)(\"div\",{className:(0,d.$)(t0().center,{[t0().center_withExplicitMark]:null==y?void 0:y.explicitDisclaimer,[t0().center_withoutExplicitMark]:!(null==y?void 0:y.explicitDisclaimer),[t0().center_spacious]:!l,[t0().center_playing]:_.isPlaying,[t0().center_withTimecode]:E||!!scrub,[t0().center_active]:!_.isGenerativeContext,VibePlayerbarMeta_scrubbing:!!scrub}),onMouseEnter:I,onMouseLeave:S,onClick:onCenterClick,onPointerDown:onCenterPointerDown,onPointerMove:onCenterPointerMove,onPointerUp:onCenterPointerUp,onPointerCancel:onCenterPointerCancel,style:scrub?{cursor:\"grabbing\",userSelect:\"none\"}:void 0,\"data-test-id\":g.e8.player.VIBE_PLAYERBAR_TIMECODE_SLIDER,children:[(0,c.jsx)(ie,{className:t0().trackName,children:F},\"\".concat(null!=(r=null==(i=_.entityMeta)?void 0:i.idWithContext)?r:\"default\",\"-\").concat(s)),(null==y?void 0:y.explicitDisclaimer)&&(0,c.jsx)(tJ.N,{containerClassName:t0().explicitMarkContainer,getDescriptionTexts:y.getDescriptionTexts,size:\"xxxs\",variant:y.explicitDisclaimer,className:t0().explicitMark,trackId:y.id}),!_.isGenerativeContext&&(0,c.jsx)(\"span\",{className:t0().timecodeOverlay,\"aria-hidden\":!0,\"data-test-id\":g.e8.player.VIBE_PLAYERBAR_TIMECODE,children:scrub?scrub.text:\"\".concat(O,\" / \").concat(M)}),!_.isGenerativeContext&&(0,c.jsx)(tq.A,{className:(0,d.$)(t0().slider,{[t0().slider_active]:!_.isGenerativeContext}),\"aria-label\":h({id:\"player-actions.timecode-control\"}),\"aria-valuetext\":scrub?scrub.text:\"\".concat(R,\" / \").concat(L),disabled:!y||v.isAdvertShown||!!scrub,style:{pointerEvents:\"none\"},onChange:W,onFocus:I,onBlur:S,maxValue:Math.round(j),mode:\"deferred\",value:Math.round(scrub?scrub.sec:w),showThumbVariant:\"never\",trackSize:\"s\",thumbSize:\"s\"}),scrub&&(0,c.jsx)(\"div\",{style:{position:\"absolute\",bottom:\"calc(100% + 12px)\",left:\"\".concat(scrub.tooltipX,\"px\"),transform:\"translateX(-50%)\",backgroundColor:\"rgba(22, 22, 26, 0.88)\",backdropFilter:\"blur(16px)\",WebkitBackdropFilter:\"blur(16px)\",color:\"#ffffff\",padding:\"4px 12px\",borderRadius:\"9999px\",fontSize:\"12px\",fontWeight:\"600\",fontVariantNumeric:\"tabular-nums\",pointerEvents:\"none\",zIndex:9999,boxShadow:\"0 4px 20px rgba(0, 0, 0, 0.4)\",whiteSpace:\"nowrap\",letterSpacing:\"0.2px\",lineHeight:\"1.4\"},children:scrub.text})]})})})'''
            content = content[:s125] + new_it + content[e125:]
            content = re.sub(r'(\$=l\.checkExperiment\(z\.z\.WebNextDisableVibeSettings,\"on\"\))\|\|[^,;]+', r'\1', content)
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print("Successfully patched 5.125+ VibePlayerBar!")
            break

        # 2. Check for 5.123.x VibePlayerbar
        start_123 = 'let t9=(0,u.PA)(()=>{var e,t,i,a,n;let{experiments:r,sonataState:s,advert:o,settings:{isMobile:l}}=(0,U.g)()'
        end_123 = ';var t4=i(56530)'
        s123 = content.find(start_123)
        e123 = content.find(end_123, s123) if s123 != -1 else -1

        if s123 != -1 and e123 != -1:
            print(f"Found 5.123.x VibePlayerBar in {os.path.basename(fpath)}")
            new_t9 = '''let t9=(0,u.PA)(()=>{var e,t,i,a,n;let{experiments:r,sonataState:s,advert:o,settings:{isMobile:l},fullscreenPlayer:fsp}=(0,U.g)(),{formatMessage:u}=(0,v.A)(),_=(0,ts.e)(),nav=(0,tm.N)(),b=s.entityMeta,p=!s.isPlaying&&s.isVibeContext,h=null!=(i=s.position)?i:0,x=null!=(a=s.duration)?a:0,[A,C]=(0,m.useState)(null),j=(0,m.useRef)(!1),{state:N,toggleTrue:P,toggleFalse:T}=(0,eo.e)(!1),k=!!x&&!s.isGenerativeContext&&N,S=j.current&&null!=A?A:h,w=x>0?Math.min(S,x)/x*100:0,I=(0,t1.E)(Math.round(S),Math.round(x)),E=(0,t1.E)(Math.round(x),Math.round(x)),O=(0,t2.P)(S),B=(0,t2.P)(x),[scrub,setScrub]=(0,m.useState)(null),dragRef=(0,m.useRef)({isDown:!1,isDragging:!1}),justScrubbedRef=(0,m.useRef)(!1);let onCenterPointerDown=(0,f.c)(e=>{if(0!==e.button||!x||x<=0)return;let target=e.currentTarget,rect=target.getBoundingClientRect();dragRef.current={isDown:!0,isDragging:!1,startX:e.clientX,startY:e.clientY,targetRect:rect,pointerId:e.pointerId,targetEl:target,lastSec:x>0?(h/x)*x:0};try{target.setPointerCapture(e.pointerId)}catch(t){}});let onCenterPointerMove=(0,f.c)(e=>{let drag=dragRef.current;if(!drag||!drag.isDown)return;let dx=e.clientX-drag.startX,dy=e.clientY-drag.startY;if(!drag.isDragging){if(Math.hypot(dx,dy)<4)return;drag.isDragging=!0}let rect=drag.targetRect,fraction=Math.max(0,Math.min(1,(e.clientX-rect.left)/rect.width)),curSec=fraction*x,fmt=e=>{let t=Math.max(0,Math.round(e)),a=Math.floor(t/60),i=t%60;return\"\"+a+\":\"+(i<10?\"0\":\"\")+i},text=fmt(curSec)+\" / \"+fmt(x),rawX=e.clientX-rect.left,minX=36,maxX=rect.width-36,tooltipX=Math.max(minX,Math.min(maxX,rawX));drag.lastSec=curSec,drag.lastRatio=fraction,setScrub({ratio:fraction,sec:curSec,tooltipX:tooltipX,text:text})});let onCenterPointerUp=(0,f.c)(e=>{let drag=dragRef.current;if(!drag||!drag.isDown)return;if(drag.isDragging){justScrubbedRef.current=!0;setTimeout(()=>{justScrubbedRef.current=!1},120);try{null==_||_.setProgress(drag.lastSec)}catch(t){}}try{drag.targetEl?.releasePointerCapture(drag.pointerId)}catch(t){}dragRef.current={isDown:!1,isDragging:!1};setScrub(null)});let onCenterPointerCancel=(0,f.c)(e=>{let drag=dragRef.current;if(drag?.isDown)try{drag.targetEl?.releasePointerCapture(drag.pointerId)}catch(t){}dragRef.current={isDown:!1,isDragging:!1};setScrub(null)});let onCenterClick=(0,f.c)(e=>{if(justScrubbedRef.current)return void(justScrubbedRef.current=!1);if(!b||s.isGenerativeContext||o.isAdvertShown)return;try{null==fsp||fsp.showFullscreenPlayerModal(),null==nav||nav({to:e8.AppScreen.PlayerScreen})}catch(t){}});let effRatio=scrub?scrub.ratio:x>0?Math.min(S,x)/x:0,effPercent=100*effRatio,M={\"--track-progress\":\"\".concat(effPercent,\"%\"),\"--progress-transition-duration\":(e=>{if(\"default\"!==e&&void 0!==e)return\"on1\"===e?\"150ms\":\"0ms\"})(null==(e=r.getExperiment(z.z.WebNextMainPlayerAnimation))?void 0:e.group),\"--progress-transition\":(j.current||scrub)?\"none\":void 0};let R=(0,m.useMemo)(()=>(0,tY.A)(()=>{T()},1e3),[T]),L=(0,f.c)((e,t)=>{o.isAdvertShown||(j.current=!t,l&&(P(),R.cancel(),R()),t?null==_||_.setProgress(e):C(e))}),W=(0,y.L)(()=>{if(s.isGenerativeContext)return(null==b?void 0:b.title)?(0,d.jsxs)(d.Fragment,{children:[(0,d.jsx)(\"span\",{className:t6().generativeIcon,children:(0,d.jsx)(Y.I,{size:\"xs\",variant:\"infinity\",\"data-test-id\":g.e8.player.VIBE_PLAYERBAR_NEUROMUSIC_ICON})}),(0,d.jsx)(\"span\",{className:t6().generativeTitle,children:b.title})]}):(0,d.jsx)(Y.I,{size:\"xs\",variant:\"infinity\",\"data-test-id\":g.e8.player.VIBE_PLAYERBAR_NEUROMUSIC_ICON});let e=[],t=[];return b&&(e.push((0,t0.X)(b.artists)),e.push(\"—\")),(null==b?void 0:b.title)&&t.push(b.title),!(null==b?void 0:b.isRemoved)&&(null==b?void 0:b.version)&&t.push(\"(\".concat(b.version,\")\")),(0,d.jsxs)(d.Fragment,{children:[e.length>0&&p&&(0,d.jsx)(\"span\",{className:t6().artists,children:e.join(\" \")}),t.join(\" \")]})});return(0,d.jsx)(\"div\",{className:t6().root,style:M,children:(0,d.jsxs)(\"div\",{className:(0,c.$)(t6().center,{[t6().center_withExplicitMark]:null==b?void 0:b.explicitDisclaimer,[t6().center_withExplicitMark_playing]:s.isPlaying,[t6().center_withoutExplicitMark]:!(null==b?void 0:b.explicitDisclaimer),[t6().center_withoutExplicitMark_playing]:s.isPlaying,[t6().center_withTimecode]:k||!!scrub,[t6().center_active]:!s.isGenerativeContext,VibePlayerbarMeta_scrubbing:!!scrub}),onMouseEnter:P,onMouseLeave:T,onClick:onCenterClick,onPointerDown:onCenterPointerDown,onPointerMove:onCenterPointerMove,onPointerUp:onCenterPointerUp,onPointerCancel:onCenterPointerCancel,style:scrub?{cursor:\"grabbing\",userSelect:\"none\"}:void 0,\"data-test-id\":g.e8.player.VIBE_PLAYERBAR_TIMECODE_SLIDER,children:[(0,d.jsx)(tQ,{className:t6().trackName,scrollingClassName:t6().scrollingTrackName,contentClassName:t6().trackNameText,pauseOnHover:!1,speed:35,gap:32,\"data-test-id\":g.e8.player.VIBE_PLAYERBAR_TRACK_NAME,children:W},\"\".concat(null!=(n=null==(t=s.entityMeta)?void 0:t.idWithContext)?n:\"default\",\"-\").concat(p)),(null==b?void 0:b.explicitDisclaimer)&&(0,d.jsx)(t8.N,{containerClassName:t6().explicitMarkContainer,getDescriptionTexts:b.getDescriptionTexts,size:\"xxxs\",variant:b.explicitDisclaimer,className:t6().explicitMark,trackId:b.id}),!s.isGenerativeContext&&(0,d.jsx)(\"span\",{className:t6().timecodeOverlay,\"aria-hidden\":!0,\"data-test-id\":g.e8.player.VIBE_PLAYERBAR_TIMECODE,children:scrub?scrub.text:\"\".concat(I,\" / \").concat(E)}),!s.isGenerativeContext&&(0,d.jsx)(tJ.A,{className:(0,c.$)(t6().slider,{[t6().slider_active]:!s.isGenerativeContext}),\"aria-label\":u({id:\"player-actions.timecode-control\"}),\"aria-valuetext\":scrub?scrub.text:\"\".concat(O,\" / \").concat(B),disabled:!b||o.isAdvertShown||!!scrub,style:{pointerEvents:\"none\"},onChange:L,onFocus:P,onBlur:T,maxValue:Math.round(x),mode:\"deferred\",value:Math.round(scrub?scrub.sec:S),showThumbVariant:\"never\",trackSize:\"s\",thumbSize:\"s\"}),scrub&&(0,d.jsx)(\"div\",{style:{position:\"absolute\",bottom:\"calc(100% + 12px)\",left:\"\".concat(scrub.tooltipX,\"px\"),transform:\"translateX(-50%)\",backgroundColor:\"rgba(22, 22, 26, 0.88)\",backdropFilter:\"blur(16px)\",WebkitBackdropFilter:\"blur(16px)\",color:\"#ffffff\",padding:\"4px 12px\",borderRadius:\"9999px\",fontSize:\"12px\",fontWeight:\"600\",fontVariantNumeric:\"tabular-nums\",pointerEvents:\"none\",zIndex:9999,boxShadow:\"0 4px 20px rgba(0, 0, 0, 0.4)\",whiteSpace:\"nowrap\",letterSpacing:\"0.2px\",lineHeight:\"1.4\"},children:scrub.text})]})})})'''
            content = content[:s123] + new_t9 + content[e123:]
            content = re.sub(r'(\$=l\.checkExperiment\(z\.z\.WebNextDisableVibeSettings,\"on\"\))\|\|[^,;]+', r'\1', content)
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print("Successfully patched 5.123.x VibePlayerBar!")
            break

def patch_wheel_fallback(inspect_dir):
    chunks_dir = os.path.join(inspect_dir, "app/_next/static/chunks")
    for fpath in glob.glob(os.path.join(chunks_dir, "*.js")):
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        if "vibe-wheel.activity-wake-up" in content and "wheelNew" in content:
            print(f"Found Wheel Store in {os.path.basename(fpath)}")
            modified = False

            target_re = r'else d\.error\("\[Wheel\] Load error",\{error:t\}\);e\.loadingState=([A-Za-z0-9_$]+)\.G\.REJECT'
            if re.search(target_re, content):
                content = re.sub(target_re, r'else d.error("[Wheel] Load error",{error:t});e.loadingState=e.items.length>0?\1.G.RESOLVE:\1.G.REJECT', content)
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
                print("Successfully patched Wheel fallback logic!")
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
    for root, _, files in os.walk(chunks_dir):
        for fname in files:
            if not fname.endswith(".js"):
                continue
            fpath = os.path.join(root, fname)
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
            if 'FreeAccess").views' in content and 'isFreeDesktopUser' in content:
                content = re.sub(
                    r'FreeAccess"\)\.views\(e=>\{let t=\{get isFreeDesktopUser\(\)\{[^}]*\},get isFreeWebUser\(\)\{[^}]*\},get isFreeUser\(\)\{[^}]*\},get isFreePlaybackDisabled\(\)\{',
                    'FreeAccess").views(e=>{let t={get isFreeDesktopUser(){return!1},get isFreeWebUser(){return!1},get isFreeUser(){return!1},get isFreePlaybackDisabled(){return!1;',
                    content
                )
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
            if "limitedFreePlayback" in content and "PREVIEW" in content:
                content = re.sub(
                    r'if\(![a-zA-Z0-9_$]+\.isAuthorized\|\|[a-zA-Z0-9_$]+\.isFreeDesktopUser\|\|[a-zA-Z0-9_$]+\|\|[a-zA-Z0-9_$]+\.limitedFreePlayback\)return\s+([a-zA-Z0-9_$.]+)PREVIEW;',
                    r'if(!1)return \1PREVIEW;',
                    content
                )
                modified = True
                print(f"Patched PREVIEW quality check in {fname}")

            # Plus unlock: Remove customDuration (29s preview duration)
            if "customDuration" in content and "isFreeDesktopUser" in content:
                content = re.sub(
                    r'customDuration:\(null==[a-zA-Z0-9_$]+\?void 0:[a-zA-Z0-9_$]+\.isAuthorized\)&&![a-zA-Z0-9_$]+\.isFreeDesktopUser\?void 0:29',
                    'customDuration:void 0',
                    content
                )
                modified = True
                print(f"Patched customDuration in {fname}")

            if modified:
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(content)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        inspect_dir = sys.argv[1]
    else:
        cand1 = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "inspect_asar"))
        cand2 = os.path.abspath(os.path.join(os.path.dirname(__file__), "inspect_asar"))
        cand3 = "/home/xox/antigravity/YandexMusicMod/inspect_asar"
        if os.path.exists(cand1):
            inspect_dir = cand1
        elif os.path.exists(cand2):
            inspect_dir = cand2
        else:
            inspect_dir = cand3
    print(f"Applying patches to: {inspect_dir}")
    patch_vibe_playerbar(inspect_dir)
    patch_wheel_fallback(inspect_dir)
    patch_modern_chunks(inspect_dir)
    patch_css(inspect_dir)
    print("All patches applied successfully!")
