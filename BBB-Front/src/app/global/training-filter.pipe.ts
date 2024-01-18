import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'trainingFilter'
})
export class TrainingFilterPipe implements PipeTransform {
  transform(trainings: any[], salle: string): any[] {
    if (!trainings) {
      return [];
    }
    if (!salle) {
      return trainings;
    }
    // return trainings.filter(training => training.salle.includes(salle));
    return trainings.filter(training => training.frequence !== 'UNE' && training.salle === salle);
  }
}
