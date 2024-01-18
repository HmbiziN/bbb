import { Component, OnInit } from '@angular/core';
import { CLUB } from 'src/app/bbb';
import { ClubService } from 'src/app/Services/club.service';

@Component({
  selector: 'app-function-team',
  templateUrl: './function-team.component.html',
  styleUrls: ['./function-team.component.css']
})
export class FunctionTeamComponent implements OnInit {
  public members: CLUB.Pole[]

  constructor(
    private clubService : ClubService
  ) { }

  ngOnInit(): void {
    this.getAllMembers();
  }

  public getAllMembers(){
    this.clubService.getTeamMembers()
    .subscribe((r:[])=>{
      this.members = r
      })
  }

}