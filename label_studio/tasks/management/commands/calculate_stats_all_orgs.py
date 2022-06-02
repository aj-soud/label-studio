from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Recalculate project stats (total_annotations, etc) for all organizations'

    def add_arguments(self, parser):
        parser.add_argument('from_scratch',
                            type=int,
                            help='Start recalculation from scratch, 0 for continuation',
                            default=0)

    def handle(self, *args, **options):
        from tasks.functions import calculate_stats_all_orgs

        calculate_stats_all_orgs(from_scratch=options['from_scratch'])
