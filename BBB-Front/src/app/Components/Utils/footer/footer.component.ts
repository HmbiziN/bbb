import { Component } from '@angular/core';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.css']
})
export class FooterComponent{
public urlFacebook : string = 'https://www.facebook.com/BasketBallBrivadois';
public urlInstagram: string = 'https://www.instagram.com/bbbrioude/';
public currentYear: number = new Date().getFullYear();

public goToWebsite(url:string){
  window.open(url, "_blank")
}

}
