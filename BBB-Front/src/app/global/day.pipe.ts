import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'day'
})
export class DayPipe implements PipeTransform {
  transform(value: string): string {
    switch (value) {
      case 'LU':
        return 'lundi';
      case 'MA':
        return 'mardi';
      case 'ME':
        return 'mercredi';
      case 'JE':
        return 'jeudi';
      case 'VE':
        return 'vendredi';
      case 'SA':
        return 'samedi';
      case 'DI':
        return 'dimanche';
      default:
        return value;
    }
  }
}
