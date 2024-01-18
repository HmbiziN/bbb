import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
    name: 'dateFilter'
})
export class DateFilterPipe implements PipeTransform {
    transform(items: any[], currentDate: Date): any[] {
        if (!items) {
            return [];
        }
        if (!currentDate) {
            currentDate = new Date();
        }
        return items.filter(item => {
            let itemDate = new Date(item.date);
            let diff = Math.floor((currentDate.getTime() - itemDate.getTime()) / (1000 * 3600 * 24));
            return diff <= 90;
        });
    }
}
