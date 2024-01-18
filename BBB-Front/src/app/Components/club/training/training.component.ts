import { Component, OnInit } from '@angular/core';
import { TRAINING } from 'src/app/bbb';
import { TrainingService } from 'src/app/Services/training.service';

export class TrainingModule { }
@Component({
  selector: 'app-training',
  templateUrl: './training.component.html',
  styleUrls: ['./training.component.css']
})
export class TrainingComponent implements OnInit {
  private readonly DAYS = ['LU', 'MA', 'ME', 'JE', 'VE', 'SA', 'DI'];
  public allTraining: TRAINING.training[] = [];
  public days = [];
  public week = {};
  public salles: string[];

  constructor(public trainingService: TrainingService) {
    this.salles = ['Salle polyvalente', 'Gymnase', 'Lycée Lafayette', 'Halle des sports'];
   }

  ngOnInit(): void {
    this.getAllTraining();
  }

  public getAllTraining() {
    this.trainingService.getAllTraining()
      .subscribe(
        (r: []) => {
          this.allTraining = r;
          this.sortTraining();
          this.days = [];
          for (let day of this.DAYS) {
            this.days.push({
              name: day,
              trainings: this.week[day]
            });
          }
        },
        (error) => {
          console.error(error);
          this.days = [];
        }
      );
  }

  public sortTraining() {
    this.week = {
    'LU': [],
    'MA': [],
    'ME': [],
    'JE': [],
    'VE': [],
    'SA': [],
    'DI': []
    };
    for (let r of this.allTraining) {
      if (this.week[r.jour]) {
        this.week[r.jour].push(r);
      }
    }
    this.days = [];
    for (let day of this.DAYS) {
      this.days.push(this.week[day]);
    }
  }  
}


