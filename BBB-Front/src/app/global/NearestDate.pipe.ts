import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'nearestDate'
})
export class NearestDatePipe implements PipeTransform {
  transform(items: any[], currentDate: Date): any[] {
    if (!items) {
      return [];
    }
    if (!currentDate) {
      currentDate = new Date();
    }

    return items.sort((a, b) => {
      const dateA = new Date(a.date);
      const dateB = new Date(b.date);
    return  Math.abs(currentDate.getTime() - dateA.getTime()) - Math.abs(currentDate.getTime() - dateB.getTime());
    });
  }
}
