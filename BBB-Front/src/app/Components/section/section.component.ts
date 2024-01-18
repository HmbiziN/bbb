import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { BehaviorSubject, Observable } from 'rxjs';
import { PLAYER } from 'src/app/bbb';
import { SectionsService } from 'src/app/Services/sections.service';

@Component({
  selector: 'app-section',
  templateUrl: './section.component.html',
  styleUrls: ['./section.component.css']
})

export class SectionComponent implements OnInit {
  public sectionId: number = 0;
  public section : any;
  public equipe: PLAYER.team[] =[]
  teams$ : BehaviorSubject<any> = new BehaviorSubject<any>(this.equipe)

  constructor(
    private route: ActivatedRoute,
    private sectionService : SectionsService
  ) { }

  ngOnInit(): void {
    this.route.params.subscribe(data => {
      switch (data.id) {
        case '1':
          this.getSection(1);
          break;
        case '2':
          this.getSection(2);
          break;
        default:
          this.getSection(3);
          break;
      }
    });
  }

  public getSection(sectionId: number) {
    this.sectionService.getSectionById(sectionId).subscribe(r => {
      this.section = r;
      this.getTeamBySection(sectionId);
    });
  }
  
  public getTeamBySection(section:number){
    this.sectionService.getTeamBySection(section)
    .subscribe({
      next:(response: any)=>
      {
        this.teams$ = response
      }
    })
  }

}
