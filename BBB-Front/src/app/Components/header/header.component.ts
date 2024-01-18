import { Component, ElementRef, Renderer2, ViewChild } from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})  
export class HeaderComponent {
  @ViewChild('bgVideo') bgVideo: ElementRef;
  @ViewChild('bgImage') bgImage: ElementRef;
  constructor(private renderer: Renderer2) {}

  ngAfterViewInit(): void {
    if (this.isMobile()) {
        this.renderer.setStyle(this.bgVideo.nativeElement, 'display', 'none');
        this.renderer.setStyle(this.bgImage.nativeElement, 'display', 'block');
    } 
    else if(!this.isMobile()){
        this.renderer.setStyle(this.bgImage.nativeElement, 'display', 'none');
        this.renderer.setStyle(this.bgVideo.nativeElement, 'display', 'block');
        this.playVideo();
    }
  }

  playVideo() {
      this.bgVideo.nativeElement.play();
      this.renderer.setStyle(this.bgImage.nativeElement, 'display', 'none');
      this.bgVideo.nativeElement.addEventListener('loadeddata', () => {
            this.bgVideo.nativeElement.addEventListener('ended', () => {
              this.renderer.setStyle(this.bgVideo.nativeElement, 'display', 'none');
              this.renderer.setStyle(this.bgImage.nativeElement, 'display', 'block');
            });
          });
  }

  isMobile(): boolean {
    if(typeof navigator === 'undefined'){
      return false;
    }
    let mobileDevices = navigator.userAgent.match(/Android|BlackBerry|iPhone|iPad|iPod|Opera Mini|IEMobile|WPDesktop/i);
    return mobileDevices != null && mobileDevices.length > 0;
  }

}


