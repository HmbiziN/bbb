import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.css']
})
export class NavComponent implements OnInit {
public urlShop : string = "https://bb-sports.fr/basket-ball-brivadois.html";
public menuMobile: boolean = false
public responsive: boolean = false
public dropdown: boolean = false
public active: boolean = false
public idSection: number = 0

  constructor(
    private router: Router
  ) { }

  ngOnInit(): void {
  }
  goToWebsite(){
    window.open(this.urlShop, "_blank")
  }
  logoMenuIsClicked(){
    this.menuMobile = true
  }
  dropdownClick(){
    this.dropdown = !this.dropdown;
  }
  clickMenu(){
    this.active=!this.active
    this.menuMobile = !this.menuMobile
  }
  goToSection(id:number){
    if(this.idSection != id){
      console.log(this.menuMobile, "m")
      this.menuMobile =false
      this.active =false
      this.idSection = id
      this.router.navigateByUrl(`section/${this.idSection}`)
    }
  }
}
