import { Component, OnInit } from '@angular/core';
import { TrainingService } from 'src/app/Services/training.service';
import { TrainingComponent } from '../training/training.component';

@Component({
  selector: 'app-exceptional-training',
  templateUrl: './exceptional-training.component.html',
  styleUrls: ['./exceptional-training.component.css']
})
export class ExceptionalTrainingComponent extends TrainingComponent implements OnInit{
  public frequence: string = 'UNE';
  futureTrainings: any[] = [];
  public isOpen = true;
  public nbrTraining = 0;
  public currentDate: Date;
  
  constructor(trainingService: TrainingService) {
    super(trainingService);
  }
  
  ngOnInit() {
    super.ngOnInit(); 
    this.trainingService.getAllTraining().subscribe(
      (r: []) => {
        this.allTraining = r;
        this.sortTraining();
        if(this.allTraining.length>0)
          this.futureTrainings = this.allTraining.filter(training => new Date(training.date) > new Date());
      },
      (error) => {
        console.error(error);
      }
    );
  }
  

  public sortTraining(): void {
    super.sortTraining();
    this.allTraining = this.allTraining.filter( (d)=> d.frequence === this.frequence);
    this.nbrTraining = this.allTraining.length
  }
}

