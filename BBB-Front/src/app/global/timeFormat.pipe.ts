import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'timeFormat'
})
export class TimeFormatPipe implements PipeTransform {

  transform(value: string): string {
    if (!value) {
      return '';
    }
    const date = new Date(`1970-01-01T${value}Z`);
    const hours = date.getHours();
    let minutes = date.getMinutes().toString();
    minutes = minutes.padStart(2, '0');
    return `${hours}h${minutes}`;
  }

}
