import { Component, OnInit } from '@angular/core';
import { PICTURES } from 'src/app/bbb';
import { GaleryService } from 'src/app/Services/galery.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-galery',
  templateUrl: './galery.component.html',
  styleUrls: ['./galery.component.css']
})

export class GaleryComponent implements OnInit {
public albums: PICTURES.Album[];

  constructor(
    private galeryService: GaleryService,
    private router: Router
  ) { 
  }

  ngOnInit(): void {
    this.getAllAlbum()
  }

  public getAllAlbum(){
    this.galeryService.getAlbum()
    .subscribe((r:PICTURES.Album[])=>{
      this.albums = r
    })
  }

  public goToDetail(id:number){
    this.router.navigateByUrl(`galerie/${id}`)
  }
}
